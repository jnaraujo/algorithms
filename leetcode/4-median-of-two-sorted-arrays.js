/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) { 
  const nums = [...nums1, ...nums2].sort((a,b) => a - b);

  const mid_arr = Math.floor((nums.length - 1) / 2);
  let median_arr = nums[mid_arr];

  if(nums.length % 2 == 0){
      median_arr += nums[mid_arr + 1];
      median_arr = median_arr / 2;
  }

  return median_arr
};