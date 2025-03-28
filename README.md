<p align="center">
   <a href="https://github.com/nichonaugle/triple-leveraged-retirement">
     <img src="https://img.shields.io/github/stars/nichonaugle/triple-leveraged-retirement?style=for-the-badge&logo=github&logoColor=white&color=yellow" alt="GitHub Stars">
   </a>
   <a href="https://github.com/nichonaugle/triple-leveraged-retirement/graphs/contributors">
     <img src="https://img.shields.io/github/contributors/nichonaugle/triple-leveraged-retirement?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Contributors">
   </a>
  <a href="https://discord.gg/xdRxUFJ44F">
    <img src="https://img.shields.io/badge/Discord-Join%20Us-blueviolet?style=for-the-badge&logo=discord&logoColor=white" alt="Join Discord">
  </a>
   <a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2741701">
    <img src="https://img.shields.io/badge/Read%20the%20Paper-View%20Now-informational?style=for-the-badge&logo=openaccess&logoColor=white" alt="View Research Paper">
  </a>
</p>

<br>

_Disclaimer: This is not financial advice, I am not a financial advisor. This repo is just a demonstration of my plan and what I am doing; something I hope you find helpful in your investment journey._

# Heavy Leverage ETF Based Retirement Strategy

My retirement portfolio bot based on a triple leveraged ETF with simple moving average for hedging. It is based on a research paper where the backtested results persist through the Great Depression. This was initially tested on the SPY but when applied to the QQQ amplified gains (and losses) can be felt. This strategy is executed in a non-retirement tax-advantaged account, so capital gains will probably need to be paid for most positions; however, the gains are worth it for smaller portfolios. The account also is based in a 5% APY cash account, which can be achieved in Robinhood (not recommended) or Webull and helps in periods where one is in a cash position. 

<p>
  Ready to supercharge your trading and support this project? 🚀
</p>

<p align="center">
  <a href="https://a.webull.com/3DbTWANtSKxdqloNpa" style="
    background-color: #4CAF50; /* Green background */
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 10px;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); /* Add shadow */
    font-weight: bold; /* Make text bold */
  ">
    Sign up using my Webull referral link! It's a win-win: you unlock a great APY on cash (which is part of this strategy), and we both score a sweet stock bonus. Your support fuels further development and research as well. Let's grow together! 💰
  </a>
</p>

## Research

_(This part is AI written because I dont want to rewrite a research paper, just go read it)_

The research paper used for this strategy is: "Leveraged ETFs: Long-Term Performance and Risk Management" by Roni Israelov and Bryan Kelly [Link](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2741701). This paper delves into the intricacies of leveraged ETFs and presents a robust strategy for managing their inherent risks. Here's a deep dive into the key findings and methodology:

**1. Leveraged ETFs and Their Characteristics**

* Leveraged ETFs aim to deliver a multiple (e.g., 2x, 3x) of the daily returns of an underlying index. This amplification also applies to losses, making them highly volatile.
* The paper highlights that due to the daily resetting mechanism, long-term returns of leveraged ETFs can deviate significantly from the leveraged multiple of the underlying index's long-term returns. This is due to the effects of compounding, especially in volatile markets. This is called Beta slippage.
* The research emphasizes the importance of understanding the compounding effects and the potential for "volatility drag," which can erode returns in choppy markets.

**2. Risk Management with Simple Moving Averages (SMA)**

* The core of the strategy is the use of a simple moving average (SMA) as a market-timing tool.
* The SMA acts as a trend-following indicator. When the price of the underlying index (e.g., SPY, QQQ) is above its SMA, the strategy invests in the leveraged ETF. When the price falls below the SMA, the strategy moves to a risk-free asset (e.g., cash).
* The paper explores various SMA lookback periods to optimize the strategy's performance.
* The SMA is used to reduce the drawdowns that leveraged ETF’s experience.

**3. Backtesting Methodology and Results**

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

**4. Key Findings and Implications**

* The research demonstrates that a well-timed strategy using leveraged ETFs and SMAs can generate superior risk-adjusted returns compared to a buy-and-hold approach.
* The SMA acts as an effective risk management tool, mitigating the impact of market downturns and reducing drawdowns.
* The strategy's robustness is evidenced by its ability to withstand significant market shocks, as shown by the backtests during the Great Depression.
* The paper also shows that the strategy works on many different underlaying assets.

**5. Application to QQQ and Amplified Volatility**

* While the paper primarily focuses on broad market indices, the strategy can be applied to other indices, such as the QQQ, which tracks the Nasdaq-100.
* Due to the QQQ's higher volatility, applying the strategy to this index can amplify both gains and losses.
* This increased volatility necessitates a careful consideration of risk tolerance and position sizing.

**Important Notes**
* I understand that a black swan day could wipe this strategy out but that assumes two things: the event happens above the sma (which historically is not likely) and you stay in the position through the event (which is irresponsible). As a result I have a stop loss implemented to prevent this from happening, but this could use some refining in the strategy.
* Leveraged ETFs are inherently risky, and this strategy is not financial advice.
* Past performance is not indicative of future results.
* It is crucial to thoroughly read and understand the linked research paper before implementing this strategy.
* Tax implications should be considered, especially when using this strategy in a non-retirement account.
* The choice of SMA length has a large impact on the performance of the strategy.
* This paper is a research paper, and is not a guarantee of future returns.
