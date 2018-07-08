# Dukum Saham

### Project Goal
Menguji beberapa teknik forecasting berbeda untuk memprekdiksi harga saham berdasarkan harga sebelumnya dan indikator sentiment analysis dari news untuk membentuk porto dengan beberapa saham untuk tujuan resiko diversifikasi. Kita melakukan ini dengan mengaplikasi metode supervised learning.

## Setup
```
$ workon myvirtualenv
[Optional]
$ pip install -r requirements.txt
$ python scripts/Algorithms/regression_models.py <input-dir> <output-dir>
```

Download dataset yang dibutuhkan untuk run code dari [sini](https://drive.google.com/open?id=0B2lCmt16L_r3SUtrTjBlRHk3d1E).

### Methodology 
1. Preprocessing and Cleaning
2. Feature Extraction
3. Twitter Sentiment Analysis and Score
4. Data Normalization
5. Analysis of various supervised learning methods
6. Conclusions

### Research Paper
- [Machine Learning in Stock Price Trend Forecasting. Yuqing Dai, Yuning Zhang](http://cs229.stanford.edu/proj2013/DaiZhang-MachineLearningInStockPriceTrendForecasting.pdf)
- [Stock Market Forecasting Using Machine Learning Algorithms. Shunrong Shen, Haomiao Jiang. Department of Electrical Engineering. Stanford University](http://cs229.stanford.edu/proj2012/ShenJiangZhang-StockMarketForecastingusingMachineLearningAlgorithms.pdf)
- [How can machine learning help stock investment?, Xin Guo](http://cs229.stanford.edu/proj2015/009_report.pdf)


### Datasets
1. http://www.nasdaq.com/
2. https://in.finance.yahoo.com
3. https://www.google.com/finance

### References
- [Scikit-Learn](http://scikit-learn.org/stable/)
- [Theano](http://deeplearning.net/software/theano/)
- [Recurrent Neural Networks - LSTM Models](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [ARIMA Models](http://people.duke.edu/~rnau/411arim.htm)
- https://github.com/dv-lebedev/google-quote-downloader
- [Book Value](http://www.investopedia.com/terms/b/bookvalue.asp)
- http://www.investopedia.com/articles/basics/09/simplified-measuring-interpreting-volatility.asp
- [Volatility](http://www.stock-options-made-easy.com/volatility-index.html)
- https://github.com/dzitkowskik/StockPredictionRNN
