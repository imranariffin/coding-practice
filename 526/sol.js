/**
 * @param {number} N
 * @return {number}
 */
const countArrangement = (N) => {
  const tkn = []
  for (let i = 0; i <= N; i++) {
    tkn.push(false)
  }
  return backtrack(tkn, 1, N)
}

// taken - Keep track of numbers that we already added to the arrangement.
// index - Current index of the arrangement [1..N].
// N     - Maximum valid number for the arrangement.
const backtrack = (taken, index, N) => {

  // We have a valid arrangement, so +1. This will bubble up to the root count.
  if (index > N) {
    return 1
  }

  let count = 0
  for (let i = 1; i <= N; i++) {

    // Make sure that our arrangements have unique numbers.
    if (taken[i]) continue

    // Only beautiful numbers pass through.
    if (i % index !== 0 && index % i !== 0) continue

    taken[i] = true

    // I think we can consider this to be a backtracking algorithm since we
    // backtrack (don't go further?) whenever the number is already taken.
    count += backtrack(taken, index + 1, N)

    taken[i] = false
  }
  return count
}
