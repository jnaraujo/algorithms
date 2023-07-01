/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
function kidsWithCandies(candies, extraCandies) {
  // best algorithm to find the highest value in an array of up to 100 elements
  const max = candies.reduce((a, b) => {
    return Math.max(a, b);
  });

  const result = new Array(candies.length);

  for (let i = 0; i < candies.length; i++) {
    result[i] = candies[i] + extraCandies >= max
  }

  return result
};

console.log(kidsWithCandies([2, 3, 5, 1, 3], 3), [true, true, true, false, true]);
console.log(kidsWithCandies([4,2,1,1,2], 1), [true,false,false,false,false]);
console.log(kidsWithCandies([12,1,12], 10), [true,false,true]);