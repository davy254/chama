const rows = document.querySelectorAll('#loans')

// for (let i = 0; i < rows.length; i++) {
    
//     let loan = rows[i].cells[2].textContent
//     let interest = parseInt(loan) * 0.1
//     rows[i].cells[3].innerHTML = interest
//     totalPayableAmount = parseInt(loan) + interest
//     rows[i].cells[4].innerHTML = totalPayableAmount
// }



// Populating interest and total payable amount
rows.forEach(row => {
    let loan = row.cells[2].textContent
    let interest = parseInt(loan) * 0.1
    row.cells[3].innerHTML = interest
    totalPayableAmount = parseInt(loan) + interest
    row.cells[4].innerHTML = totalPayableAmount
});


// getting all interest generated
const interestGen = document.getElementById('interest-gen')
totalInterest=0
rows.forEach(row => {
    totalInterest += Number(row.cells[3].textContent)
    interestGen.innerHTML= 'The total interest earned is sh. ' + totalInterest
});

// Highlighting loan status with color
const loanStatus = document.querySelectorAll('#loan-status')

console.log(loanStatus)

loanStatus.forEach(loan => {
    loan.textContent === "PENDING" ? loan.style.backgroundColor = 'red': loan.style.backgroundColor = 'green'
    loan.style.color = 'floralWhite'
});