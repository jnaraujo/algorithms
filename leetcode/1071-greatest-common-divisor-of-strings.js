/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
function gcdOfStrings(str1, str2) {
  if(str1 + str2 == str2 + str1){
    return str1.slice(0,gcd(str1.length, str2.length))
  }

  return ""
}

/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
function gcd(a, b) {
  if (!b) return a;
  return gcd(b, a % b)
}

console.log(gcdOfStrings("ABCABC", "ABC"), "ABC");
console.log(gcdOfStrings("ABABAB", "ABAB"), "AB");
console.log(gcdOfStrings("LEET", "CODE"), "");
console.log(gcdOfStrings("ABCDEF", "ABC"), "");
console.log(gcdOfStrings("ABABABAB", "ABAB"), "ABAB");
console.log(gcdOfStrings("AAAAAAAAA", "AAACCC"), "");
console.log(gcdOfStrings("ABABABAB", "ABAB"), "ABAB");
console.log(gcdOfStrings("CXTXNCXTXNCXTXNCXTXNCXTXN", "CXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXN"), "CXTXN");