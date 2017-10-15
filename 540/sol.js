/**
 * @param {number[]} nums
 * @return {number}
 */
const singleNonDuplicate = (nums) => {

  // Iterate through nums and keep track of the number count via a map.
  const countMap = {}
  nums.forEach(num => {
    if (!countMap.hasOwnProperty(num)) {
      countMap[num] = 0
    }
    countMap[num] += 1
  })

  // There should be a number with a count of 1 in the map. Just find it and
  // return the value.
  return Object.entries(countMap).reduce((res, pair) => {
    if (!res && pair[1] === 1) {
      return res = new Number(pair[0])
    }
    return res
  }, null)
}
