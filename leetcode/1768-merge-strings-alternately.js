/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
function mergeAlternately(word1, word2) {
  let word = []

  for (let i = 0; i < Math.max(word1.length, word2.length); i++) {
    if (i > word1.length - 1) {
      word.push(...word2.slice(i, word2.length))
      return word.join("")
    }
    if (i > word2.length - 1) {
      word.push(...word1.slice(i, word1.length))
      return word.join("")
    }

    word.push(word1[i], word2[i])
  }

  return word.join("")
}

console.log(mergeAlternately("abc", "pqr"), "apbqcr")
console.log(mergeAlternately("ab", "pqrs"), "apbqrs")
console.log(mergeAlternately("abcd", "pq"), "apbqcd")
