/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
function isAnagram(s, t) {
  if (s.length !== t.length) return false

  const charCount = new Map()

  for (const letter of t) {
    charCount.set(letter, (charCount.get(letter) || 0) + 1)
  }

  for (const letter of s) {
    if (!charCount.has(letter) || charCount.get(letter) === 0) {
      return false
    }
    charCount.set(letter, charCount.get(letter) - 1)
  }

  return true;
}

console.log(isAnagram("anagram", "nagaram"), true)
console.log(isAnagram("rat", "car"), false)