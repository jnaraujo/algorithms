function lengthOfLongestSubstring(s: string): number {
  const longestSubstring = new Map();
  let streak = 0;
  let start = 0;

  for(let i = 0; i < s.length; i++){
      const letter = s[i];

      if(longestSubstring[letter] !== undefined){
          start = Math.max(longestSubstring[letter] + 1, start);
      }

      streak = Math.max(streak, i - start + 1);

      longestSubstring[letter] = i;
  }

  return streak;
};