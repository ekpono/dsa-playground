const number = [8, 5, null, 7, 2, null, 4, null, 3, 4, null];
// [ [1,5], [7, 2], [4] ]

let total = [];
let startNewArray = true;

for (i = 0; i < number.length; i++) {
  const arrayInsert = total.length - 1;

  if (number[i] === null) {
    startNewArray = true;
  } else {
    if (startNewArray) {
      total.push([number[i]]);
      startNewArray = false;
    } else {
      total[arrayInsert].push(number[i]);
    }
  }
}

console.log(total);
