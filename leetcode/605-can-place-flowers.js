/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
function canPlaceFlowers(flowerbed, n) {
  let count = 0;

  for (let i = 0; i < flowerbed.length; i++) {
    if (!flowerbed[i - 1] && !flowerbed[i] && !flowerbed[i + 1]) {
      count += 1
      i += 1
    }

    if (count >= n) {
      return true;
    }
  }

  return false;
};

console.log(canPlaceFlowers([1, 0, 0, 0, 1], 1) === true);
console.log(canPlaceFlowers([1, 0, 0, 0, 1], 2) === false);
console.log(canPlaceFlowers([1, 0, 1, 0, 1], 1) === false);
console.log(canPlaceFlowers([1, 0, 0], 1) === true);
console.log(canPlaceFlowers([0, 1, 0], 1) === false);
console.log(canPlaceFlowers([0, 0, 1, 0, 1], 1) === true);
console.log(canPlaceFlowers([0, 0, 1, 0, 0], 2) === true);
console.log(canPlaceFlowers([1, 0, 0, 0, 1], 1) === true);
console.log(canPlaceFlowers([1, 0, 0, 0, 0, 1], 2) === false);
console.log(canPlaceFlowers([1, 0, 0, 0, 0, 0, 0, 1], 3) === false);
console.log(canPlaceFlowers([0, 0, 1, 0], 1) === true);