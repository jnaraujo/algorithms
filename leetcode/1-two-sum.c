/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
  int* pos = (int *) malloc(sizeof(int) * 2);
  
  *returnSize = 2;
  
  pos[0] = -1;
  pos[1] = -1;
  
  for(int i = 0; i < numsSize; i++){
      for(int j = i+1; j < numsSize; j++){
          if(nums[i] + nums[j] == target){
              pos[0] = i;
              pos[1] = j;
          }

      }
      
      if(pos[0] != -1 && pos[1] != -1){
          return pos;
      }
  }
  
  return pos;
}