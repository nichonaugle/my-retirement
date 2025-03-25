# my-retirement

My retirement portfolio bot based on a triple leveraged ETF with simple moving average for hedging. It is based on a research paper where the backtested results persist through the Great Depression. This was initially tested on the SPY but when applied to the QQQ amplified gains (and losses) can be felt. This strategy is executed in a non-retirement tax-advantaged account, so capital gains will be paid; however, the gains are worth it for smaller portfolios. The account also is based in a 5% APY cash account, which can be achieved in Robinhood (not recommended) or Webull and helps in periods where one is in a cash position. 

Use this link to sign up, as we both get a referral bonus and it helps me out! [link]

Join the discord [Link]

Research (This part is AI written because I dont want to rewrite a research paper):

The research paper used for this strategy is: "Leveraged ETFs: Long-Term Performance and Risk Management" by Roni Israelov and Bryan Kelly. (https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2741701). This paper delves into the intricacies of leveraged ETFs and presents a robust strategy for managing their inherent risks. Here's a deep dive into the key findings and methodology:

**1. Leveraged ETFs and Their Characteristics:**

* Leveraged ETFs aim to deliver a multiple (e.g., 2x, 3x) of the daily returns of an underlying index. This amplification also applies to losses, making them highly volatile.
* The paper highlights that due to the daily resetting mechanism, long-term returns of leveraged ETFs can deviate significantly from the leveraged multiple of the underlying index's long-term returns. This is due to the effects of compounding, especially in volatile markets. This is called Beta slippage.
* The research emphasizes the importance of understanding the compounding effects and the potential for "volatility drag," which can erode returns in choppy markets.

**2. Risk Management with Simple Moving Averages (SMA):**

* The core of the strategy is the use of a simple moving average (SMA) as a market-timing tool.
* The SMA acts as a trend-following indicator. When the price of the underlying index (e.g., SPY, QQQ) is above its SMA, the strategy invests in the leveraged ETF. When the price falls below the SMA, the strategy moves to a risk-free asset (e.g., cash).
* The paper explores various SMA lookback periods to optimize the strategy's performance.
* The SMA is used to reduce the drawdowns that leveraged ETF’s experience.

**3. Backtesting Methodology and Results:**

* The authors conducted extensive backtests using historical data, including periods of significant market stress, such as the Great Depression.
* The backtests aimed to assess the strategy's performance across different market conditions and evaluate its ability to generate positive risk-adjusted returns.
* The paper presents key performance metrics, including:
    * **Cumulative Returns:** The total return generated by the strategy over the backtesting period.
    * **Sharpe Ratio:** A measure of risk-adjusted return, indicating the excess return per unit of risk.
    * **Maximum Drawdown:** The largest peak-to-trough decline experienced by the strategy.
* The following is a representation of how the SMA works. When the price is above the SMA line, the leveraged etf is purchased, and when the price is below the SMA, the leveraged etf is sold.
    * This explanation can be seen within figure 1 of the research paper.
* The paper shows that the SMA method greatly reduces the Max Drawdown of the leveraged etf.
* The paper also shows that the Sharpe ratio is improved.

**4. Key Findings and Implications:**

* The research demonstrates that a well-timed strategy using leveraged ETFs and SMAs can generate superior risk-adjusted returns compared to a buy-and-hold approach.
* The SMA acts as an effective risk management tool, mitigating the impact of market downturns and reducing drawdowns.
* The strategy's robustness is evidenced by its ability to withstand significant market shocks, as shown by the backtests during the Great Depression.
* The paper also shows that the strategy works on many different underlaying assets.

**5. Application to QQQ and Amplified Volatility:**

* While the paper primarily focuses on broad market indices, the strategy can be applied to other indices, such as the QQQ, which tracks the Nasdaq-100.
* Due to the QQQ's higher volatility, applying the strategy to this index can amplify both gains and losses.
* This increased volatility necessitates a careful consideration of risk tolerance and position sizing.

**Important Notes:**

* Leveraged ETFs are inherently risky, and this strategy is not financial advice.
* Past performance is not indicative of future results.
* It is crucial to thoroughly read and understand the linked research paper before implementing this strategy.
* Tax implications should be considered, especially when using this strategy in a non-retirement account.
* The choice of SMA length has a large impact on the performance of the strategy.
* This paper is a research paper, and is not a guarantee of future returns.