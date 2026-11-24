> Past performance does predict future results -- if you check for stationarity first.

```
What Makes Time Series Different:-
Standard ML assumes i.i.d. -- independent and identically distributed. Each sample is drawn from the same distribution, independently of other samples. Time series violates both:

    - Not independent. Today's stock price depends on yesterday's. This week's sales correlate with last week's.
    - Not identically distributed. The distribution shifts over time. Sales in December look different from sales in March.
```

# Every time series is a combination of:
1. Trend: The long-term direction. Revenue growing 10% per year. Global temperature rising.
2. Seasonality: Repeating patterns at fixed intervals. Retail sales spike in December. Air conditioning usage peaks in July.
3. Residual: Whatever is left after removing trend and seasonality. If the residual looks like white noise, the decomposition captured the signal.

>Autocorrelation
Autocorrelation measures how much a value at time tt correlates with the value at time t−kt−k (kk steps in the past). The autocorrelation function (ACF) plots this correlation for each lag kk.

ACF tells you:
    - How far back the series remembers. If ACF drops to zero after lag 5, values more than 5 steps ago are irrelevant.
    - Whether seasonality exists. If ACF spikes at lag 12 (monthly data), there is yearly seasonality.
    - How many lag features to create. Use lags up to where ACF becomes negligible.

PACF (Partial Autocorrelation Function) removes indirect correlations. If today correlates with 3 days ago only because both correlate with yesterday, PACF at lag 3 will be zero while ACF at lag 3 will not.

```
ARIMA Intuition

ARIMA is the classical time series model. It has three components:

    AR (Autoregressive): Predict from past values. AR(p) uses the last pp values.
    I (Integrated): Differencing to achieve stationarity. I(d) applies dd rounds of differencing.
    MA (Moving Average): Predict from past forecast errors. MA(q) uses the last qq errors.

ARIMA(p, d, q) combines all three. You choose pp, dd, qq based on ACF/PACF analysis or automated search (auto-ARIMA).

We will not implement ARIMA from scratch -- it requires numerical optimization that is beyond the scope of this lesson. The key insight is understanding what each component does so you can interpret ARIMA results and know when to use it.

```