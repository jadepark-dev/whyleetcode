/*
 * @lc app=leetcode id=238 lang=typescript
 *
 * [238] Product of Array Except Self
 * Product: 곱하기의 결과물(곱셈의 결과)
 */

// @lc code=start
function productExceptSelf(nums: number[]): number[] {
  // nums = [1,2,3,4]
  const l = nums.length
  // 같은 길이의 배열을 1로 채워서 초기화
  // [1,1,1,1]
  const leftToRight = new Array(l).fill(1)
  const rightToLeft = new Array(l).fill(1)
  const res = new Array(l).fill(1)

  for (let i = 1; i < l; i++) {
    leftToRight[i] = leftToRight[i - 1] * nums[i - 1] // nums[0], nums[1], .. nums[3]
    // [1,1,1,1]
    // [1, 2, 3, 4 ]
    // [ 1, 1, 2, 6 ]
    rightToLeft[l - i - 1] = rightToLeft[l - i] * nums[l - i] // nums[3], nums[2], .. nums[0]
    // [ 24, 12, 4, 1 ]
  }

  console.log('leftToRight', leftToRight)
  console.log('rightToLeft', rightToLeft)

  for (let i = 0; i < l; i++) {
    res[i] = leftToRight[i] * rightToLeft[i]
  }

  return res
}
// @lc code=end
