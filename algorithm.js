// const search = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// const value = 11;

// const binarySearch = (search, value) => {
//   let found = null;
//   let middleIndex = Math.floor(search.length / 2);

//   for (let i = 0; i <= middleIndex; i++) {
//     if (search[middleIndex] > value) {
//       search = search.splice(0, middleIndex);
//       middleIndex = Math.floor(search.length / 2);
//     }

//     if (search[middleIndex] < value) {
//       search = search.splice(middleIndex);
//       middleIndex = Math.floor(search.length / 2);
//     }

//     if (search[middleIndex] === value) {
//       i = middleIndex;
//       found = `found: ${search[middleIndex]} with index of ${i}`;
//     }
//   }

//   return found;
// };

// console.log(binarySearch(search, value));

let unsortedArray = [5, 6, 3, 2, 1, 4];

const bubbleSort = (unsortedArray) => {
  for (let i = 0; i < unsortedArray.length - 1; i++) {
    for (let j = 0; j < unsortedArray.length - i - 1; j++) {
      if (unsortedArray[j] > unsortedArray[j + 1]) {
        const temp = unsortedArray[j];
        unsortedArray[j] = unsortedArray[j + 1];
        unsortedArray[j + 1] = temp;
        console.log(unsortedArray);
      }
    }
    console.log("-=========---");
  }

  return unsortedArray;
};

console.log(bubbleSort(unsortedArray));
