# Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


**Example 1:**

Input: prices = [7,1,5,3,6,4]

Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


**Example 2:**

Input: prices = [7,6,4,3,1]

Output: 0

Explanation: In this case, no transactions are done and the max profit = 0.
 

## Constraints:

1 <= prices.length <= 105

0 <= prices[i] <= 104

------------------------------------------------------------------------

## 🧠 Key Insight (Core Idea)

**~To maximize profit:**

Buy at the lowest price

Sell at a higher price later

**~While scanning prices:**

Keep track of the minimum price seen so far

For each day, calculate the profit if sold today

Keep updating the maximum profit

---------------------------------------------------------------------------

## 🪜 Approach (One-Pass Greedy)

**~ Initialize:**

min_price → very large value

max_profit → 0

**~Loop through prices:**

Update min_price if current price is lower

Calculate profit = current_price - min_price

Update max_profit

Return max_profit

----------------------------------------------------------------------------

## ✅ Why This Works

You always buy before selling

You only care about the lowest buying price before today

One pass → optimal and efficient

------------------------------------------------------------------------------

## 🧪 Example Walkthrough

Input:

prices = [7, 1, 5, 3, 6, 4]

Day	 Price	 MinPrice	 Profit	 Max Profit

0	    7	     7  	     0	         0

1	    1	     1	       0	         0

2	    5	     1	       4	         4

3	    3	     1	       2	         4

4	    6	     1	       5	         5

5	    4	     1	       3	         5

✅ Answer = 5

--------------------------------------------------------------------------------

## ⏱ Time & Space Complexity

Time: O(n)
Space: O(1)

---------------------------------------------------------------------------------

## 🚫 Common Mistakes

❌ Nested loops → O(n²) (TLE)

❌ Selling before buying

❌ Overthinking with all combinations

---------------------------------------------------------------------------------
## 🔑 Pattern Name (Important for Interviews)

Greedy

Min so far / Max difference

Kadane-like thinking

---------------------------------------------------------------------------------
