# Estimating latent asset-pricing factors✩

# Martin Lettau a,b,c, Markus Pelger d,∗

a Haas School of Business, University of California at Berkeley, Berkeley, CA 94720, United States of America 

b NBER, United States of America 

c CEPR, United Kingdom 

d Department of Management Science & Engineering, Stanford University, Stanford, CA 94305, United States of America 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/55e9774501de99fe7ab5f93fc87d6078ddcc606724e383003da47f536824617a.jpg)


# a r t i c l e i n f o

Article history: 

Received 8 May 2018 

Received in revised form 16 December 2018 

Accepted 5 August 2019 

Available online 1 February 2020 

JEL classification: 

C14 

C38 

C52 

C58 

G12 

Keywords: 

Cross section of returns 

Anomalies 

Expected returns 

High-dimensional data 

Latent factors 

Weak factors 

PCA 

# a b s t r a c t

We develop an estimator for latent factors in a large-dimensional panel of financial data that can explain expected excess returns. Statistical factor analysis based on Principal Component Analysis (PCA) has problems identifying factors with a small variance that are important for asset pricing. We generalize PCA with a penalty term accounting for the pricing error in expected returns. Our estimator searches for factors that can explain both the expected return and covariance structure. We derive the statistical properties of the new estimator and show that our estimator can find asset-pricing factors, which cannot be detected with PCA, even if a large amount of data is available. Applying the approach to portfolio data we find factors with Sharpe-ratios more than twice as large as those based on conventional PCA and with smaller pricing errors. 

© 2020 Elsevier B.V. All rights reserved. 

# 1. Introduction

Approximate factor models have been a heavily researched topic in finance and macroeconomics in the last years (see Bai and Ng (2008), Stock and Watson (2006) and Ludvigson and Ng (2010)). The most popular technique to estimate latent factors is Principal Component Analysis (PCA) of a covariance or correlation matrix. It estimates factors that can best explain the co-movement in the data. A situation that is often encountered in practice is that the explanatory power of the factors is weak relative to idiosyncratic noise. In this case conventional PCA performs poorly (see Onatski (2012)). In some cases economic theory also imposes structure on the first moments of the data. Including this additional information in the estimation turns out to significantly improve the estimation of latent factors, in particular for those factors with a weak explanatory power in the variance. 

We suggest a new statistical method to find the most important factors for explaining the variation and the mean in a large dimensional panel. Our key application are asset pricing factors. The fundamental insight of asset pricing theory is that the cross-section of expected returns should be explained by exposure to systematic risk factors.1 Hence, asset pricing factors should simultaneously explain time-series covariation as well as the cross-section of mean returns. Finding the ‘‘right’’ risk factors is not only the central question in asset pricing but also crucial for optimal portfolio and risk management. 2 Traditional PCA methods based on the covariance or correlation matrices identify factors that capture only common time-series variation but do not take the cross-sectional explanatory power of factors into account.3 We generalize PCA by including a penalty term to account for the pricing errors in the means. Hence, our estimator Risk-Premium PCA (RP-PCA) directly includes the object of interest, which is explaining the cross-section of expected returns, in the estimation. It turns out, that even if the goal is to explain the covariation and not the mean, the additional information in the mean can improve the estimation significantly. 

This paper develops the asymptotic inferential theory for our estimator under a general approximate factor model and shows that it dominates conventional estimation based on PCA if there is information in the mean. We distinguish between strong and weak factors in our model. Strong factors essentially affect all underlying assets. The market-wide return is an example of a strong factor in asset pricing applications. RP-PCA can estimate these factors more efficiently than PCA as it efficiently combines information in first and second moments of the data. Weak factors affect only a subset of the underlying assets and are harder to detect. Many asset-pricing factors fall into this category. RP-PCA can find weak factors with high Sharpe-ratios, which cannot be detected with PCA, even if an infinite amount of data is available. 

We build upon the econometrics literature devoted to estimating factors from large dimensional panel data sets. The general case of a static large dimensional factor model is treated in Bai (2003), Bai and Ng (2002). Forni et al. (2000) introduce the dynamic principal component method. Fan et al. (2013) study an approximate factor structure with sparsity. Aït-Sahalia and Xiu (2017) and Pelger (2019) extend the large dimensional factor model to high-frequency data. All these methods assume a strong factor structure that is estimated with some version of PCA without taking into account the information in expected returns, which results in a loss of efficiency. We generalize the framework of Bai (2003) to include the pricing error penalty and show that it only effects the asymptotic distribution of the estimates but not consistency. 

Onatski (2012) studies principal component estimation of large factor models with weak factors. He shows that if a factor does not explain a sufficient amount of the variation in the data, it cannot be detected with PCA. We provide a solution to this problem that renders weak factors with high Sharpe-ratios detectable. Our statistical model extends the spiked covariance model from random matrix theory used in Onatski (2012) and Benaych-Georges and Nadakuditi (2011) to include the pricing error penalty. We show that including the information in the mean leads to larger systematic eigenvalues of the factors, which reduces the bias in the factor estimation and makes weak factors detectable. The derivation of our results is challenging as we cannot make the standard assumption that the mean of the stochastic processes is zero. As many asset pricing factors can be characterized as weak, our estimation approach becomes particularly relevant. 

Our work is part of the emerging econometrics literature that combines latent factor extraction with a form of regularization. Bai and Ng (2017) develop the statistical theory for robust principal components. Their estimator can be understood as performing iterative ridge instead of least squares regressions, which shrinks the eigenvalues of the common components to zero. They combine their shrunk estimates with a clean-up step that sets the small eigenvalues to zero. Their estimates have less variation at the cost of a bias. Our approach also includes a penalty which in contrast is based on economic information and does not create a bias–variance trade-off. The objective of finding factors that can explain co-movements and the cross-section of expected returns simultaneously is based on the fundamental insight of arbitrage pricing theory. We show theoretically and empirically that including the additional information of arbitrage pricing theory in the estimation of factors leads to factors that have better out-of-sample pricing performance. Our estimator depends on a tuning parameter that trades off the information in the variance and the mean in the data. Our statistical theory provides guidance on the optimal choice of the tuning parameter that we confirm in simulations and in the data. 

Our work is closely related to the paper by Fan and Zhong (2018) which allows estimating latent factors based on an over-identifying set of moments. We combine the first and second moments to estimate factors while their approach allows the inclusion of additional moments. Their analysis is based on a generalized method of moment approach under the assumption of a finite cross-section. Our strong factor model formulation can be similarly related to a general method of moment problem. We consider a large number of assets and include the additional perspective of a weak factor model which we think is particularly relevant in the context of asset pricing factors. 

We apply our methodology to monthly returns of 370 decile sorted portfolios based on relevant financial anomalies for 55 years. We find that five factors can explain very well these expected returns and strongly outperform PCA-based factors. The maximum Sharpe-ratio of our five factors is more than twice as large as those based on PCA; a result that holds in- and out-of-sample. The pricing errors out-of-sample are sizably smaller. Our method captures the pricing information better while explaining the same amount of variation and co-movement in the data. Our companion paper (Lettau and Pelger, 2020) provides a more in-depth empirical analysis of asset-pricing factors estimated with our approach. 

The rest of the paper is organized as follows. In Section 2 we introduce the model and provide an intuition for our estimators. Section 3 discusses the formal objective function that defines our estimator. Section 4 provides the inferential theory for strong factors, while 5 presents the asymptotic theory for weak factors. Section 6 provides Monte Carlo simulations demonstrating the finite-sample performance of our estimator. In Section 7 we study the factor structure in a large equity data set. Section 8 concludes. The Appendix contains the proofs.4 

# 2. Factor model

We assume that excess returns follow a standard approximate factor model and the assumptions of the arbitrage pricing theory are satisfied. This means that returns have a systematic component captured by K factors and a nonsystematic, idiosyncratic component capturing asset-specific risk. The approximate factor structure allows the non-systematic risk to be weakly dependent. We observe the excess5 return of N assets over T time periods:6 

$$
X _ {t, i} = F _ {t} ^ {\top} \Lambda_ {i} + e _ {t, i} \quad i = 1, \dots , N t = 1, \dots , T.
$$

In matrix notation this reads as 

$$
\underbrace {X} _ {T \times N} = \underbrace {F} _ {T \times K} \underbrace {\Lambda^ {\top}} _ {K \times N} + \underbrace {e} _ {T \times N}.
$$

Our goal is to estimate the unknown latent factors F and the loadings Λ. We will work in a large dimensional panel, i.e. the number of cross-sectional observations N and the number of time-series observations T are both large and we study the asymptotics for them jointly going to infinity. 

Assume that the factors and residuals7 are uncorrelated. This implies that the covariance matrix of the returns consists of a systematic and idiosyncratic part: 

$$
\operatorname{Var} \left(X _ {t}\right) = \Lambda \operatorname{Var} \left(F _ {t}\right) \Lambda^ {\top} + \operatorname{Var} \left(e _ {t}\right).
$$

Under standard assumptions the largest eigenvalues of Var(X) are driven by the factors. This motivates Principal Component Analysis (PCA) as an estimator for the loadings and factors. Essentially all estimators for latent factors only utilize the information contained in the second moment, but ignore information that is contained in the first moment. 

Arbitrage-Pricing Theory (APT) has a second implication: The expected excess return is explained by the exposure to the risk factors multiplied by the risk-premium of the factors. If the factors are excess returns APT implies 

$$
E [ X _ {t, i} ] = E [ F _ {t} ] ^ {\top} \Lambda_ {i}.
$$

Here we assume a strong form of APT, where residual risk has a risk-premium of zero. In its more general form APT requires only the risk-premium of the idiosyncratic part of well-diversified portfolios to go to zero. As most of our analysis will be based on portfolios, there is no loss of generality by assuming the strong form. 

Factors constructed by PCA explain as much common time-series variation as possible. Conventional statistical factor analysis applies PCA to the sample covariance matrix $\scriptstyle { \frac { 1 } { T } } X ^ { \top } X - { \bar { X } } { \bar { X } } ^ { \top }$ where X¯ denotes the sample mean of excess returns. The eigenvectors of the largest eigenvalues are proportional to the loadings $\hat { \boldsymbol A } ^ { \mathrm { P C A } }$ . Factors are obtained from a regression on the estimated loadings. It can be shown that conventional PCA factor estimates are based on the time-series variation objective function, where $\tilde { X } _ { t } = X _ { t } - \bar { X }$ and $\tilde { F } _ { t } = F _ { t } - \bar { F }$ denotes the demeaned returns respectively factors: 

$$
\min _ {\Lambda , \tilde {F}} \frac {1}{N T} \sum_ {i = 1} ^ {N} \sum_ {t = 1} ^ {T} (\tilde {X} _ {t i} - \tilde {F} _ {t} ^ {\top} \Lambda_ {i}) ^ {2}
$$

We call our approach Risk-Premium-PCA (RP-PCA). It applies PCA to a covariance matrix with overweighted mean 

$$
\frac {1}{T} X ^ {\top} X + \gamma \bar {X} \bar {X} ^ {\top}
$$

with the risk-premium weight $\gamma .$ The eigenvectors of the largest eigenvalues are proportional to the loadings $\hat { \boldsymbol A } ^ { \mathrm { R P - P C A } }$ . We show that RP-PCA minimizes jointly the unexplained variation and pricing error: 

$$
\min _ {\varLambda , F} \underbrace {\frac {1}{N T} \sum_ {i = 1} ^ {N} \sum_ {t = 1} ^ {T} (\tilde {X} _ {t i} - \tilde {F} _ {t} ^ {\top} \varLambda_ {i}) ^ {2}} _ {\text { unexplained   variation }} + (1 + \gamma) \underbrace {\frac {1}{N} \sum_ {i = 1} ^ {N} \left(\bar {X} _ {i} - \bar {F} ^ {\top} \varLambda_ {i}\right) ^ {2}} _ {\text { pricing   error }},
$$

Factors are estimated by a regression of the returns on the estimated loadings, i.e. $\hat { \boldsymbol { F } } = X \hat { \boldsymbol { \Lambda } } \left( \hat { \boldsymbol { A } } ^ { \intercal } \hat { \boldsymbol { \Lambda } } \right) ^ { - 1 }$ . 

We develop the statistical theory that provides guidance on the optimal choice of the key parameter $\gamma .$ . There are essentially two different factor model interpretations: a strong factor model and a weak factor model. In a strong factor model the factors provide a strong signal and lead to exploding eigenvalues in the covariance matrix relative to the idiosyncratic eigenvalues. This is either because the strong factors affect a very large number of assets and/or because they have very large variances themselves. In a weak factor model the factors’ signals are weak and the resulting eigenvalues are large compared to the idiosyncratic spectrum, but they do not explode.8 In both cases it is always optimal to choose $\gamma \neq - 1$ , i.e. it is better to use our estimator instead of PCA applied to the covariance matrix. In a strong factor model, the estimates become more efficient. In a weak factor model it strengthens the signal of the weak factors, which could otherwise not be detected. Depending on which framework is more appropriate, the optimal choice of $\gamma$ varies. A weak factor model usually suggests much larger choices for the optimal $\gamma$ than a strong factor model. However, in strong factor models our estimator is consistent for any choice of $\gamma$ and choosing a too large $\gamma$ results in only minor efficiency losses. On the other hand a too small $\gamma$ can prevent weak factors from being detected at all. Thus in our empirical analysis we opt for the choice of larger $\gamma \mathbf { \dot { s } }$ . 

We derive the statistical theory separately for the strong and the weak factor model. In a model that contains both, strong and weak factors, we can first consistently estimate the strong factors and project them out. The residuals from the strong factor model can then be described by a weak factor model. 

The empirical spectrum of eigenvalues in equity data suggests a combination of strong and weak factors. In all the equity data that we have tested the first eigenvalue of the sample covariance matrix is very large, typically around ten times the size of the rest of the spectrum. The second and third eigenvalues usually stand out, but have only magnitudes around twice or three times of the average of the residual spectrum, which would be more in line with a weak factor interpretation. The first statistical factor in our data sets is always very strongly correlated with an equally-weighted market factor. Hence, if we are interested in learning more about factors besides the market, the weak factor model might provide better guidance. 

# 3. Objective function

This section explains the relationship between our estimator and the objective function that is minimized. We introduce the following notation: 1 is a vector $T \times 1$ of 1’s and thus $F ^ { \top } \mathbb { 1 } / T$ is the sample mean of F . The projection matrix $M _ { \Lambda } \ = \ I _ { N } - \bar { \Lambda ( } \Lambda ^ { \top } { \varLambda } ) ^ { - 1 } { \varLambda } ^ { \top }$ annihilates the K−dimensional vector space spanned by Λ. $I _ { N }$ and $I _ { T }$ denote the N- respectively T -dimensional identity matrix. The projection matrix $\begin{array} { r } { M _ { 1 } = I _ { N } - \frac { 1 } { T } \mathbb { 1 } \dot { \mathbb { 1 } } ^ { \top } } \end{array}$ demeans the time-series, i.e. ${ \tilde { X } } =$ $M _ { 1 } X$ and ${ \tilde { \cal F } } = M _ { 1 } { \cal F }$ . 

The objective function of conventional statistical factor analysis is to minimize the sum of squared errors for the crosssection and time dimension, i.e. the estimator $\hat { \boldsymbol A }$ and $\hat { F }$ are chosen to minimize the unexplained variance. This variation objective function is 

$$
\min _ {\varLambda , \tilde {F}} \frac {1}{N T} \sum_ {i = 1} ^ {N} \sum_ {t = 1} ^ {T} (\tilde {X} _ {t i} - \tilde {F} _ {t} ^ {\top} \varLambda_ {i}) ^ {2} = \min _ {\varLambda} \frac {1}{N T} \operatorname{trace} \left((\tilde {X} M _ {\varLambda}) ^ {\top} (\tilde {X} M _ {\varLambda})\right) \quad \text {with} \tilde {F} = \tilde {X} \varLambda^ {\top} (\varLambda^ {\top} \varLambda) ^ {- 1}.
$$

The second formulation makes use of the fact that in a large panel data set the factors can be estimated by a regression of the assets on the loadings, $F = X ( A ^ { \top } A ) ^ { - 1 } A ^ { \top }$ , and hence the demeaned residuals equal $\tilde { X } - \tilde { F } A ^ { \top } = X M _ { \varLambda } .$ . This is equivalent to choosing Λˆ proportional to the eigenvectors of the first K largest eigenvalues of $\begin{array} { r } { \frac { 1 } { N T } \tilde { X } ^ { \top } \tilde { X } = \frac { 1 } { N T } \tilde { X ^ { \top } } M _ { 1 } X = } \end{array}$ $\begin{array} { r } { \frac { 1 } { N T } X ^ { \top } \left( I _ { T } - \frac { \mathbb { 1 1 } ^ { \top } } { T } \right) X . ^ { 9 } } \end{array}$ ) X .9 

Arbitrage-pricing theory predicts that the factors should price the cross-section of expected excess returns. This yields a pricing objective function which minimizes the cross-sectional pricing error: 

$$
\min _ {\Lambda , F} \frac {1}{N} \sum_ {i = 1} ^ {N} \left(\frac {1}{T} X _ {i} ^ {\top} \mathbb {1} - \frac {1}{T} F ^ {\top} \mathbb {1} \Lambda_ {i} ^ {\top}\right) ^ {2} = \min _ {\Lambda} \frac {1}{N} \operatorname{trace} \left(\left(\frac {1}{T} \mathbb {1} ^ {\top} X M _ {\Lambda}\right) \left(\frac {1}{T} \mathbb {1} ^ {\top} X M _ {\Lambda}\right) ^ {\top}\right).
$$

However, the cross-sectional objective function does not identify a set of factors and loadings and the problem admits an infinite number of solutions. Specifically, any Λ such that $X ^ { \top } \mathbb { I }$ belongs to the space spanned by Λ will be a solution. 

We propose to combine these two objective functions with the risk-premium weight $\gamma .$ . The idea is to obtain statistical factors that explain the co-movement in the data and produce small pricing errors: 

$$
\begin{array}{l} \min _ {\Lambda , F} \frac {1}{N T} \operatorname{trace} \left(\left((\tilde {X} M _ {\Lambda}) ^ {\top} (\tilde {X} M _ {\Lambda})\right)\right) + (1 + \gamma) \frac {1}{N} \operatorname{trace} \left(\left(\frac {1}{T} \mathbb {1} ^ {\top} X M _ {\Lambda}\right) \left(\frac {1}{T} \mathbb {1} ^ {\top} X M _ {\Lambda}\right) ^ {\top}\right) \\ = \min _ {\Lambda} \frac {1}{N T} \operatorname{trace} \left(M _ {\Lambda} X ^ {\top} \left(I + \frac {\gamma}{T} \mathbb {1 1} ^ {\top}\right) X M _ {\Lambda}\right) \quad \text { with } F = X \Lambda^ {\top} (\Lambda^ {\top} \Lambda) ^ {- 1}. \\ \end{array}
$$

Here, we have made use of the linearity of the trace operator. The objective function is minimized by the eigenvectors of the largest eigenvalues of $\begin{array} { r } { \frac { 1 } { N T } X ^ { \top } \left( I _ { T } \dot { + } \frac { \gamma } { T } \mathbb { 1 } \mathbb { 1 } ^ { \top } \right) } \end{array}$ X. Hence the factors and loadings can be obtained by applying PCA to this new matrix. The estimator for the loadings Λˆ are the eigenvectors of the first K eigenvalues of √ $\begin{array} { r } { \frac { 1 } { N T } X ^ { \top } \left( I _ { T } + \frac { \gamma } { T } \mathbb { 1 } \mathbb { 1 } ^ { \top } \right) } \end{array}$ X multiplied by $\sqrt { N } . \ \hat { F }$ are $\scriptstyle { \frac { 1 } { N } } X { \hat { \boldsymbol { A } } }$ . The estimator for the common component $C = F A$ is simply $\hat { \boldsymbol { C } } = \hat { \boldsymbol { F } } \hat { \boldsymbol { A } } ^ { \top }$ . The estimator simplifies to PCA of the covariance matrix for $\gamma = - 1$ . 

In practice conventional PCA is often applied to the correlation instead of the covariance matrix. This implies that the returns are demeaned and normalized by their standard-deviation before applying PCA. Hence, factors are chosen that explain most of the correlation instead of the variance. This approach is particularly appealing if the underlying panel data is measured in different units. Usually, estimation based on the correlation matrix is more robust than based on the covariance matrix as it is less affected by a few outliers with very large variances. From a statistical perspective this is equivalent to applying a cross-sectional weighting matrix to the panel data. After applying PCA, the inverse of the weighting matrix has to be applied to the estimated eigenvectors. The statistical rationale is that certain cross-sectional observations contain more information about the systematic risk than others and hence should obtain a larger weight in the statistical analysis. The standard deviation of each cross-sectional observation serves as a proxy for how large the noise is and therefore down-weighs very noisy observations. 

Mathematically, a weighting matrix means that instead of minimizing equally weighted pricing errors we apply a weighting function $\tilde { Q }$ to the cross-section resulting in the following weighted combined objective function: 

$$
\begin{array}{l} \min _ {\Lambda , F} \frac {1}{N T} \operatorname{trace} (\tilde {Q} ^ {\top} (\tilde {X} - \tilde {F} \Lambda^ {\top}) ^ {\top} (\tilde {X} - \tilde {F} \Lambda^ {\top}) \tilde {Q}) \\ + (1 + \gamma) \frac {1}{N} \operatorname{trace} \left(\frac {1}{T} \mathbb {1} ^ {\top} (X - F \Lambda^ {\top}) \tilde {Q} \tilde {Q} ^ {\top} (X - F \Lambda^ {\top}) ^ {\top} \mathbb {1} \frac {1}{T}\right) \\ = \min _ {\Lambda} \frac {1}{N T} \operatorname{trace} \left(M _ {\Lambda} \tilde {Q} ^ {\top} X ^ {\top} \left(I + \frac {\gamma}{T} \mathbb {1 1} ^ {\top}\right) X \tilde {Q} M _ {\Lambda}\right) \\ \text { with } F = X \varLambda^ {\top} (\varLambda^ {\top} \varLambda) ^ {- 1}. \\ \end{array}
$$

Therefore factors and loadings can be estimated by applying PCA to $\begin{array} { r } { \tilde { \boldsymbol { \mathsf { Q } } } ^ { \top } \boldsymbol { X } ^ { \top } \left( \boldsymbol { I } + \frac { \gamma } { T } \mathbb { 1 } \mathbb { 1 } ^ { \top } \right) \boldsymbol { X } \tilde { \boldsymbol { \mathsf { Q } } } } \end{array}$ . In our empirical application we only consider the weighting matrix $\tilde { Q }$ which is the inverse of a diagonal matrix of standard deviations of each return. For $\gamma = - 1$ this corresponds to using a correlation matrix instead of a covariance matrix for PCA. 

There are four different interpretations of RP-PCA: 

(1) Variation and pricing objective functions: Our estimator combines a variation and pricing error criteria function. As such it only selects factors that are priced and hence have small cross-sectional alpha’s. But at the same time it protects against spurious factors that have vanishing loadings as it requires the factors to explain a large amount of the variation in the data as well.10 

(2) Penalized PCA: RP-PCA is a generalization of PCA regularized by a pricing error penalty term. Factors that minimize the variation criterion need to explain a large part of the variance in the data. Factors that minimize the cross-sectional pricing criterion need to have a non-vanishing risk-premia. Our joint criteria is essentially looking for the factors that explain the time-series but penalizes factors with a low Sharpe-ratio. Hence the resulting factors usually have much higher Sharpe-ratios than those based on conventional factor analysis. 

(3) Information interpretation: Conventional PCA of a covariance matrix only uses information contained in the second moment but ignores all information in the first moment. As using all available information leads in general to more efficient estimates, there is an argument for including the first moment in the objective function. Our estimator can be seen as combining two moment conditions efficiently. This interpretation drives the results for the strong factor model in Section 4. 

(4) Signal-strengthening: The matrix $\bar { \tau } X ^ { \top } X + \gamma \bar { X } \bar { X } ^ { \top }$ should converge ${ \mathrm { t o } } ^ { 1 1 }$ 

$$
\Lambda \left(\Sigma_ {F} + (1 + \gamma) \mu_ {F} \mu_ {F} ^ {\top}\right) \Lambda^ {\top} + \operatorname{Var} (e),
$$

where $\textstyle \sum _ { F } = \operatorname { V a r } ( F _ { t } )$ denotes the covariance matrix of F and $\mu _ { F } = E [ F _ { t } ]$ the mean of the factors. After normalizing the loadings, the strengths of the factors in the standard PCA of a covariance matrix are equal to their variances. Larger factor variances will result in larger systematic eigenvalues and a more precise estimation of the factors. In our RP-PCA the signal of weak factors with a small variance can be ‘‘pushed up’’ by their mean if $\gamma$ is chosen accordingly. In this sense our estimator strengthens the signal of the systematic part. This interpretation is the basis for the weak factor model studied in Section 5. 

# 4. Strong factor model

In a strong factor model RP-PCA provides a more efficient estimator of the loadings than PCA. Both RP-PCA and PCA provide consistent estimator for the loadings and factors. In the strong factor model, the systematic factors are so strong that they lead to exploding eigenvalues relative to the idiosyncratic eigenvalues. This is captured by the assumption that ${ \frac { 1 } { N } } \varLambda ^ { \top } \varLambda \to \varSigma _ { \varLambda }$ where $\Sigma _ { A }$ is a full-rank matrix.12 This could be interpreted as the strong factors affecting an infinite number of assets. 

The estimator for the loadings $\hat { \boldsymbol A }$ are the eigenvectors of the first K eigenvalues of ${ \textstyle \frac { 1 } { N } } \left( { \frac { 1 } { T } } X ^ { \top } X + \gamma { \bar { X } } { \bar { X } } ^ { \top } \right)$ ) multiplied by $\sqrt { N }$ . Up to rescaling the estimators are identical to those in the weak factor model setup. The estimator for the common component $C = F \bar { A } \mathrm { i } s \hat { C } = \hat { F } \hat { A } ^ { \top }$ . 

Bai (2003) shows that under Assumption 1 the PCA estimator of the loadings has the same asymptotic distribution as an OLS regression of X on the true factors F (up to a rotation). Similarly, the estimator for the factors behaves asymptotically like an OLS regression of $X ^ { \top }$ on the true loadings Λ (up to a rotation). Under slightly stronger assumptions we will show that the estimated loadings under RP-PCA have the same asymptotic distribution up to rotation as an OLS regression of WX on WF with $\begin{array} { r } { W ^ { 2 } = \left( I _ { T } + \gamma \frac { \mathbb { 1 1 } } { T } \right) } \end{array}$ . Surprisingly, the estimated factors under RP-PCA and PCA have the same asymptotic distribution when N .13 ${ \frac { \sqrt { N } } { T } } . 1 3$ 

Assumption 1 is identical to Assumptions A–G in Bai (2003) and some additional weak assumptions related to the mean. More specifically, we add assumptions about the time-series mean in D.2, E.1, E.2 and E.4 to Bai (2003)’s assumptions and slightly modify A, C.3 and F. The Supplementary Appendix provides a detailed comparison between our and Bai (2003)’s assumptions. We denote by $\begin{array} { r } { \bar { F } _ { t } = \frac { 1 } { T } \sum _ { t = 1 } ^ { T } F } \end{array}$ and $\begin{array} { r } { \bar { \boldsymbol { e } } _ { i } = \frac { 1 } { T } \sum _ { t = 1 } ^ { T } \boldsymbol { e } _ { t , i } } \end{array}$ the time-series mean of the factors and idiosyncratic component. The correlation structure in the residuals can be more general in the strong model than in the weak model. This comes at the cost of larger values for the loading vectors. The residuals still need to satisfy a form of sparsity assumption restricting the dependence. The strong factor model provides a distribution theory which is based on a central limit theorem of the residuals. 

# Assumption 1 (Strong Factor Model).

A: Factors: $E [ \| F _ { t } \| ^ { 4 } ] \le M < \infty$ and $\begin{array} { r } { { \frac { 1 } { T } } \sum _ { t = 1 } ^ { T } F _ { t } \stackrel { p } { \to } \mu _ { F } } \end{array}$ and $\begin{array} { r } { F ^ { \top } ( I _ { T } + \frac { \gamma } { T } \mathbb { 1 } \mathbb { 1 } ^ { \top } ) F \stackrel { p } {  } \Sigma _ { F } + ( 1 + \gamma ) \mu _ { F } \mu _ { F } ^ { \top } } \end{array}$ which is a $K \times K$ positive definite matrix. 

B: Factor loadings: $\| A _ { i } \| < \infty$ , and $\| A ^ { \top } A / N - \Sigma _ { A } \| \to 0$ for some $K \times K$ positive definite matrix $\Sigma _ { A }$ . 

C: Time and cross-section dependence and heteroskedasticity: There exists a positive constant $M < \infty$ such that for all N and T : 

1. $E [ e _ { t , i } ] = 0 , E [ | e _ { t , i } | ^ { 8 } ] \leq M .$ 

$\begin{array} { r } { E [ N ^ { - 1 } \sum _ { i = 1 } ^ { N } e _ { s , i } e _ { t , i } ] = \xi ( s , t ) , | \xi ( s , s ) | \le M } \end{array}$ N for all s and for every $t \leq T$ it holds $\begin{array} { r } { \sum _ { s = 1 } ^ { T } | \xi ( s , t ) | \le M } \end{array}$ 

3. $E [ e _ { t , i } e _ { s , j } ] = \tau _ { i j , t s }$ with $| \tau _ { i j , t s } | \le | \tau _ { i j } |$ for some $\tau _ { i j }$ and for all s, t and for every $i \leq N$ it holds $\textstyle \sum _ { i = 1 } ^ { N } | \tau _ { i j } | \leq M$ 

$E [ e _ { t , i } e _ { s , j } ] = \tau _ { i j , t s }$ and $\begin{array} { r } { ( N T ) ^ { - 1 } \sum _ { i = 1 } ^ { N } \sum _ { j = 1 } ^ { N } \sum _ { t = 1 } ^ { T } \sum _ { s = 1 } ^ { T } | \tau _ { i j , s t } | \leq M . } \end{array}$ 

5. For every $\begin{array} { r } { ( t , s ) , E \left[ | N ^ { - 1 / 2 } \sum _ { i = 1 } ^ { N } ( e _ { s , i } e _ { t , i } ) - E [ e _ { s , t } e _ { t , i } ] | ^ { 4 } \right] \leq M . } \end{array}$ 

D: Weak dependence between factors and idiosyncratic errors: 

1. $\begin{array} { r } { E \left[ \frac { 1 } { N } \sum _ { i = 1 } ^ { N } \| \frac { 1 } { \sqrt { T } } \sum _ { t = 1 } ^ { T } F _ { t } e _ { t , i } \| ^ { 2 } \right] \leq M . } \end{array}$ 

2. $\begin{array} { r } { E \left[ \frac { 1 } { N } \sum _ { i = 1 } ^ { N } \| \sqrt { T } \bar { F } \bar { e } _ { i } \| ^ { 2 } \right] \leq M . } \end{array}$ 

E: Moments and Central Limit Theorem: There exists an $M < \infty$ such that for all N and T : 

1. For each $\begin{array} { r } { t , E \left[ \left. \frac { 1 } { \sqrt { N T } } \sum _ { s = 1 } ^ { T } \sum _ { k = 1 } ^ { N } F _ { s } ( e _ { s , k } e _ { t , k } - E [ e _ { s , k } e _ { t , k } ] ) \right. ^ { 2 } \right] \leq M } \end{array}$ and 

$$
E \left[ \left\| \frac {\sqrt {T}}{\sqrt {N}} \sum_ {k = 1} ^ {N} \bar {F} \left(\bar {e} _ {k} e _ {t, k} - E [ \bar {e} _ {k} e _ {t, k} ]\right) \right\| ^ {2} \right] \leq M.
$$

2. The $K \times K$ matrices satisfy $\begin{array} { r } { E \left[ \| \frac { 1 } { \sqrt { N T } } \sum _ { t = 1 } ^ { T } \sum _ { i = 1 } ^ { N } F _ { t } \boldsymbol { \Lambda } _ { i } ^ { \top } \boldsymbol { e } _ { t , i } \| ^ { 2 } \right] \leq M } \end{array}$ and 

$$
E \left[ \| \frac {\sqrt {T}}{\sqrt {N}} \sum_ {i = 1} ^ {N} \bar {F} \Lambda_ {i} ^ {\top} \bar {e} _ {i} \| ^ {2} \right] \leq M.
$$

3. For each t as $N \to \infty ;$ 

$$
\frac {1}{\sqrt {N}} \sum_ {i = 1} ^ {N} \Lambda_ {i} e _ {t, i} \xrightarrow {d} N (0, \Gamma_ {t}),
$$

where $\begin{array} { r } { T _ { t } = \operatorname* { l i m } _ { N  \infty } \frac { 1 } { N } \sum _ { i = 1 } ^ { N } \sum _ { j = 1 } ^ { N } { A _ { i } A _ { j } ^ { \top } E [ e _ { t , i } e _ { t , j } ] } . } \end{array}$ 

4. For each i as $T \to \infty ;$ 

$$
\binom{\frac {1}{\sqrt {T}} \sum_ {t = 1} ^ {T} F _ {t} e _ {t, i}}{\frac {1}{\sqrt {T}} \sum_ {t = 1} ^ {T} e _ {t, i}} \xrightarrow {D} N (0, \varOmega_ {i}) \qquad \varOmega_ {i} = \left( \begin{array}{c c} \varOmega_ {1 1, i} & \varOmega_ {1 2, i} \\ \varOmega_ {2 1, i} & \varOmega_ {2 2, i} \end{array} \right)
$$

$\begin{array} { r } { \mathrm { w h e r e ~ } \varOmega _ { i } = p \operatorname* { l i m } _ { T \to \infty } \frac { 1 } { T } \sum _ { s = 1 } ^ { T } \sum _ { t = 1 } ^ { T } E \left[ \left( F _ { t } F _ { s } ^ { \top } e _ { s , i } e _ { t , i } \quad F _ { t } e _ { s , i } e _ { t , i } \right) \right] . } \end{array}$ 

F: The eigenvalues of the $K \times K$ matrix $\Sigma _ { A } ( \Sigma _ { F } + ( \gamma + 1 ) \mu _ { F } \mu _ { F } ^ { \top } )$ are distinct. 

Assumption A and B are standard in the literature and require the factors and loadings to be systematic, i.e. the factors affect a number of assets that is proportional to N. Assumption C is essentially identical to Bai (2003) and restricts the time-series and cross-sectional correlation in the residuals. It requires a form of sparsity in the residuals covariance and autocorrelation matrices that allows for example for an ARMA-type time-series correlation and block-correlation structure in the cross-section. Assumption D allows the factors and residuals to depend weakly on each other and does not require independence. Assumption E is only needed for the asymptotic distribution. It assumes the existence of central limit theorems and the boundedness of the necessary higher moments. As mentioned before, we add assumptions related to the mean to E.1 and E.2 compared to the standard framework of Bai (2003). These assumptions are very weak and not required if for example the factors and residuals are independent. The additional central limit theorem in E.4 related to $\textstyle { \frac { 1 } { \sqrt { T } } } \sum _ { t = 1 } ^ { T } e _ { t , i }$ is satisfied for any appropriate martingale difference sequence. 

Theorem 1 provides the inferential theory for the strong factor model. 

Theorem 1 (Asymptotic Distribution in Strong Factor Model). Assume Assumption 1 holds and min $( N , T ) \to \infty .$ . Then: 

1. For any $\gamma \in [ - 1 , \infty )$ the factors and loadings can be estimated consistently component-wise. 

$\begin{array} { r } { I f \ \frac { \sqrt { T } } { N }  0 , } \end{array}$ , then the asymptotic distribution of the loading estimator is given by 

$$
\sqrt {T} \left(H ^ {\top} \hat {\Lambda} _ {i} - \Lambda_ {i}\right) \xrightarrow {D} N (0, \Phi_ {i})
$$

$$
\Phi_ {i} = \left(\Sigma_ {F} + (\gamma + 1) \mu_ {F} \mu_ {F} ^ {\top}\right) ^ {- 1} \left(\Omega_ {1 1, i} + \gamma \mu_ {F} \Omega_ {2 1, i} + \gamma \Omega_ {1 2, i} \mu_ {F} ^ {\top} + \gamma^ {2} \mu_ {F} \Omega_ {2 2, i} \mu_ {F} ^ {\top}\right) \left(\Sigma_ {F} + (\gamma + 1) \mu_ {F} \mu_ {F} ^ {\top}\right) ^ {- 1}
$$

$$
H = \left(\frac {1}{T} F ^ {\top} W ^ {2} F\right) \left(\frac {1}{N} \Lambda \hat {\Lambda}\right) V _ {T N} ^ {- 1}
$$

and $V _ { T N }$ is a diagonal matrix of the largest K eigenvalues of $\textstyle { \frac { 1 } { N T } } X ^ { \top } W ^ { 2 } X$ and $\begin{array} { r } { W ^ { 2 } = \left( I _ { T } + \gamma \frac { \mathbb { 1 1 } ^ { \top } } { T } \right) } \end{array}$ . 

3. $\begin{array} { r } { I f \ \frac { \sqrt { N } } { T }  0 , } \end{array}$ , then the asymptotic distribution of the factors is not affected by the choice of $\gamma .$ . 

4. For any choice of $\gamma \in [ - 1 , \infty )$ the common components can be estimated consistently if $\operatorname* { m i n } ( N , T ) \to \infty .$ . The asymptotic distribution of the common component depends on $\gamma \ i f$ and only $i f N / T$ does not go to zero. For $T / N \to 0$ 

$$
\sqrt {T} \left(\hat {C} _ {t, i} - C _ {t, i}\right) \xrightarrow {D} N \left(0, F _ {t} ^ {\top} \Phi_ {i} F _ {t}\right).
$$

Note that Bai (2003) characterizes the distribution of $\sqrt { T } \left( A _ { i } - H ^ { \top ^ { - 1 } } \hat { \lambda } _ { i } \right)$ , while we rotate the estimated loadings $\sqrt { T } \left( H ^ { \top } \hat { \lambda } _ { i } - \varLambda _ { i } \right)$ . Our rotated estimators are directly comparable for different choices of $\gamma .$ . The proof is delegated to the Supplementary Appendix, where we show how to map our problem into Bai’s (2003) framework. The key argument is based on an asymptotic expansion. Under Assumption 1 we can show that the following expansions hold 

$\begin{array} { r } { \mathrm { 1 . ~ } \sqrt { T } \left( H ^ { \top } \hat { \lambda } _ { i } - \varLambda _ { i } \right) = \left( \frac { 1 } { T } F ^ { \top } W ^ { 2 } F \right) ^ { - 1 } \frac { 1 } { \sqrt { T } } F ^ { \top } W ^ { 2 } e _ { i } + O _ { p } \left( \frac { \sqrt { T } } { N } \right) + o _ { p } ( 1 ) } \end{array}$ 

$\begin{array} { r } { 2 . \ \sqrt { N } \left( H ^ { \top - 1 } \hat { F } _ { t } - F _ { t } \right) = \left( \frac { 1 } { N } \Lambda ^ { \top } \boldsymbol { A } \right) ^ { - 1 } \frac { 1 } { \sqrt { N } } \boldsymbol { A } ^ { \top } \boldsymbol { e } _ { t } ^ { \top } + O _ { p } \left( \frac { \sqrt { N } } { T } \right) + o _ { p } ( 1 ) } \end{array}$ 

$\begin{array} { r } { 3 . \sqrt { \delta } \left( \hat { C } _ { t , i } - C _ { t , i } \right) = \frac { \sqrt { \delta } } { \sqrt { T } } F _ { t } ^ { \top } \left( \frac { 1 } { T } F ^ { \top } W ^ { 2 } F \right) ^ { - 1 } \frac { 1 } { \sqrt { T } } F ^ { \top } W ^ { 2 } e _ { i } + \frac { \sqrt { \delta } } { \sqrt { N } } A _ { i } ^ { \top } \left( \frac { 1 } { N } A ^ { \top } A \right) ^ { - 1 } \frac { 1 } { \sqrt { N } } A ^ { \top } e _ { t } ^ { \top } + o _ { p } ( 1 ) } \end{array}$ with $\delta = \operatorname* { m i n } ( N , T )$ . 

We just need to replace the factors and asset space by their projected counterpart WF and WX in Bai’s (2003) proofs. Conventional PCA, i.e. $\gamma = - 1$ is a special case of our result, which typically leads to inefficient estimation. In order to get a better intuition we consider an example with i.i.d. residuals over time. This simplified model will be more comparable to the weak factor model in the next section. 

Example 1 (Simplified Strong Factor Model). 

1. Rate: Assume that N, $T \to \infty$ and $\begin{array} { r } { \frac { N } { T }  c } \end{array}$ with $0 < c < \infty .$ . 

2. Factors: The factors F are uncorrelated among each other and are independent of e and Λ and have bounded first four moments. 

$$
\hat {\mu} _ {F} := \frac {1}{T} \sum_ {t = 1} ^ {T} F _ {t} \stackrel {{p}} {{\to}} \mu_ {F} \qquad \hat {\Sigma} _ {F} := \frac {1}{T} \sum_ {t = 1} ^ {T} F _ {t} F _ {t} ^ {\top} - \hat {\mu} \hat {\mu} ^ {\top} \stackrel {{p}} {{\to}} \Sigma_ {F} = \left( \begin{array}{c c c} \sigma_ {F _ {1}} ^ {2} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & \sigma_ {F _ {K}} ^ {2} \end{array} \right).
$$

3. Loadings: $A ^ { \top } A / N \ { \overset { p } { \to } } \ I _ { K }$ and all loadings are bounded. The loadings are independent of the factors and residuals. 

4. Residuals: The residual matrix can be represented as $e = \epsilon \Sigma ^ { 1 / 2 }$ with $\epsilon _ { t , i } \stackrel { i . i . d . } { \sim } N ( 0 , 1 )$ . All elements and all row sums of absolute values of Σ are bounded. 

Corollary 1 (Simplified Strong Factor Model). Assume that the assumptions of Example 1 hold. Then, the factors and loadings can be estimated consistently. The asymptotic distribution of the factors is not affected by γ . The asymptotic distribution of the loadings is given by 

$$
\sqrt {T} \left(H ^ {\top} \hat {\Lambda} _ {i} - \Lambda_ {i}\right) \xrightarrow {D} N (0, \Omega_ {i}),
$$

where $E [ e _ { t , i } ^ { 2 } ] = \sigma _ { e _ { i } } ^ { 2 }$ and 

$$
\Omega_ {i} = \sigma_ {e _ {i}} ^ {2} \left(\Sigma_ {F} + (1 + \gamma) \mu_ {F} \mu_ {F} ^ {\top}\right) ^ {- 1} \left(\Sigma_ {F} + (1 + \gamma) ^ {2} \mu_ {F} \mu_ {F} ^ {\top}\right) \left(\Sigma_ {F} + (1 + \gamma) \mu_ {F} \mu_ {F} ^ {\top}\right) ^ {- 1}.
$$

The optimal choice for the weight minimizing the asymptotic variance is $\gamma = 0$ . Choosing $\gamma = - 1$ , i.e. the covariance matrix for factor estimation, is not efficient. 

The estimator in the strong factor model can be formulated as a GMM problem. Up to a remainder term that vanishes under appropriate rate conditions the loading estimator is given by 

$$
H ^ {\top} \hat {\Lambda} _ {i} = \left(F ^ {\top} W ^ {2} F\right) ^ {- 1} F ^ {\top} W ^ {2} X _ {i}.
$$

This is equivalent to combining the OLS and the pricing moment conditions with a weight γ . More specifically, we define the following K + 1 population and sample moments 

$$
\varPi (\varLambda_ {i}) = E \left[ \binom{(X _ {t, i} - F _ {t} ^ {\top} \varLambda_ {i}) F _ {t} (E [ F _ {t} F _ {t} ^ {\top} ]) ^ {- 1 / 2}}{X _ {i} - F _ {t} ^ {\top} \varLambda_ {i}} \right] \qquad \hat {\varPi} (\varLambda_ {i}) = \binom{\frac {1}{\sqrt {T}} (X _ {i} - F \varLambda_ {i}) ^ {\top} F (F ^ {\top} F) ^ {- 1 / 2}}{\frac {1}{T} (X _ {i} - F \varLambda_ {i}) ^ {\top} \mathbb {1}}.
$$

The first K moments are identical to the OLS first order condition of a regression of X on F . The last moment is the APT pricing moment equation. The GMM estimator 

$$
\operatorname{argmin} \hat {\Pi} ^ {\top} \left( \begin{array}{c c} I _ {K} & 0 \\ 0 & \gamma \end{array} \right) \hat {\Pi}
$$

has the solution $H ^ { \top } \hat { \boldsymbol { A } } _ { i } .$ . 

# 5. Weak factor model

If factors are weak rather than strong, RP-PCA can detect factors that are not estimated by conventional PCA. Weak factors affect only a smaller fraction of the assets. After normalizing the loadings, a weak factor can be interpreted as having a small variance. If the variance of a weak factor is below a critical value, it cannot be detected by PCA. However, the signal of RP-PCA depends on the mean and the variance of the factors. Thus, RP-PCA can detect weak factors with a high Sharpe-ratio even if their variance is below the critical detection value. Weak factors can only be estimated with a bias but the bias will generally be smaller for RP-PCA than for PCA. 

In a weak factor model $\varLambda ^ { \intercal } \varLambda$ is bounded in contrast to a strong factor model in which $\textstyle { \frac { 1 } { N } } A ^ { \top } A$ is bounded. The statistical model for analyzing weak factor models is based on spiked covariance models from random matrix theory. It is wellknown that under the theory assumptions of random matrix the eigenvalues of a sample covariance matrix separate into two areas: (1) the bulk spectrum with the majority of the eigenvalues that are clustered together and (2) some spiked large eigenvalues separated from the bulk. Under appropriate assumptions the bulk spectrum converges to the generalized Marcenko–Pastur distribution. The largest eigenvalues are estimated with a bias which is characterized by the Stieltjes ˘ transform of the generalized Marcenko–Pastur distribution. If the largest population eigenvalues are below some critical ˘ threshold, a phase transition phenomena occurs. The estimated eigenvalues will vanish in the bulk spectrum and the corresponding estimated eigenvectors will be orthogonal to the population eigenvectors.14 

The estimator of the loadings Λˆ are the first K eigenvectors of $\bar { \tau } X ^ { \top } X \bar { + } \gamma \bar { X } \bar { X } ^ { \top }$ . Conventional PCA of the sample covariance matrix corresponds to $\gamma = - 1 . ^ { 1 5 }$ The estimators of the factors are the regression of the returns on the loadings, i.e. $\hat { \boldsymbol F } = \boldsymbol X \hat { \boldsymbol A }$ . 

# 5.1. Assumptions

We impose the following assumptions on the approximate factor model: 

Assumption 2 (Weak Factor Model). 

A: Rate: Assume that $N , T \to \infty$ and $N / T  c$ with $0 < c < \infty$ . 

B: Factors: The factors F are uncorrelated among each other and are independent of e and Λ and have bounded first two moments. 

$$
\hat {\mu} _ {F} := \frac {1}{T} \sum_ {t = 1} ^ {T} F _ {t} \stackrel {{p}} {{\to}} \mu_ {F} \qquad \hat {\Sigma} _ {F} := \frac {1}{T} \sum_ {t = 1} ^ {T} F _ {t} F _ {t} ^ {\top} - \hat {\mu} \hat {\mu} ^ {\top} \stackrel {{p}} {{\to}} \Sigma_ {F} = \left( \begin{array}{c c c} \sigma_ {F _ {1}} ^ {2} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & \sigma_ {F _ {K}} ^ {2} \end{array} \right).
$$

C: Loadings: $A ^ { \top } A \stackrel { p } { \to } I _ { K }$ and the column vectors of the loadings Λ are orthogonally invariant $( \mathbf { e . g . ~ } A _ { i , k } \sim N ( 0 , 1 / N )$ and independent of the factors and residuals. 

D: Residuals: The matrix of residuals can be represented as $e = \epsilon \Sigma ^ { 1 / 2 }$ with $\epsilon _ { t , i } \stackrel { i . i . d . } { \sim } N ( 0 , 1 )$ . The empirical eigenvalue distribution function of Σ converges almost surely weakly to a non-random spectral distribution function with compact support. The supremum of the support is b and the largest eigenvalues of Σ converge to b. 

Assumption 2.C can be interpreted as considering only well-diversified portfolios as factors. It essentially assumes that the portfolio weights of the factors are random with a variance of 1/N. The orthogonally invariance assumption on the loading vectors is satisfied if for example ${ A _ { i , k } } \stackrel { i . i . d . } { \sim } N ( 0 , 1 / N )$ . This is certainly a stylized assumption, but it allows us to derive closed-form solutions that are easily interpretable.16 Assumption 2.D is a standard assumption in random matrix theory.17 The assumption allows for non-trivial weak cross-sectional correlation in the residuals, but excludes serial-correlation. It implies clustering of the largest eigenvalues of the population covariance matrix of the residuals and rules out that a few linear combinations of idiosyncratic terms have an unusually large variation which could not be separated from the factors. It can be weakened as in Onatski (2012) when considering estimation based on the covariance matrix. However, when including the risk-premium in the estimation it seems that the stronger assumption is required. Many relevant cross-sectional correlation structures are captured by this assumption e.g. sparse correlation matrices or an ARMA-type dependence. 

# 5.2. Asymptotic results

In order to state the results for the weak factor model, we need to define several well-known objects from random matrix theory. We define the average idiosyncratic noise as $\sigma _ { e } ^ { 2 } : = \mathrm { t r a c e } ( \Sigma ) / N$ , which is the average of the eigenvalues of Σ . If the residuals are i.i.d. distributed, $\sigma _ { e } ^ { 2 }$ would simply be their variance. Our estimator will depend strongly on the dependency structure of the residual covariance matrix which can be captured by its eigenvalues. Denote by $\lambda _ { 1 } \geq \lambda _ { 2 } \geq \dots \geq \lambda _ { N }$ the ordered eigenvalues of $\scriptstyle { \frac { 1 } { T } } e ^ { \top } e$ . The Cauchy transform of the almost sure limit of the empirical distribution of the eigenvalues is: 

$$
G (z) = a. s. \lim _ {T, N \rightarrow \infty} \frac {1}{N} \sum_ {i = 1} ^ {N} \frac {1}{z - \lambda_ {i}} = a. s. \lim _ {T, N \rightarrow \infty} \frac {1}{N} \operatorname{trace} \left(\left(z I _ {N} - \frac {1}{T} e ^ {\top} e\right) ^ {- 1}\right).
$$

This function is well-defined for z outside the support of the limiting spectral distribution. This Cauchy transform is a well-understood object in random matrix theory. For simple cases analytical solutions exist and for general Σ it can easily be simulated or estimated from the data. 

A second important transformation of the residual eigenvalues is 

$$
B (z) = a. s. \lim _ {T, N \rightarrow \infty} \frac {c}{N} \sum_ {i = 1} ^ {N} \frac {\lambda_ {i}}{(z - \lambda_ {i}) ^ {2}} = a. s. \lim _ {T, N \rightarrow \infty} \frac {c}{N} \operatorname{trace} \left(\left(z I _ {N} - \frac {1}{T} e ^ {\top} e\right) ^ {- 2} \left(\frac {1}{T} e ^ {\top} e\right)\right).
$$

For special cases a closed-form solution for the function $B ( z )$ is available and for the general case it can be easily estimated. 

The crucial tool for understanding RP-PCA is the concept of a ‘‘signal matrix’’ M. The signal matrix essentially represents the largest population eigenvalues. For PCA estimation based on the sample covariance matrix the signal matrix $M _ { \mathrm { P C A } }$ equals:18 

$$
M _ {\mathrm{PCA}} = \Sigma_ {F} + c \sigma_ {e} ^ {2} I _ {K} = \left( \begin{array}{c c c} \sigma_ {F _ {1}} ^ {2} + c \sigma_ {e} ^ {2} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & \sigma_ {F _ {K}} ^ {2} + c \sigma_ {e} ^ {2} \end{array} \right)
$$

and the ‘‘signals’’ are the K largest eigenvalues $\theta _ { 1 } ^ { \mathsf { P C A } } , \hdots , \theta _ { K } ^ { \mathsf { P C A } }$ of this matrix. The ‘‘signal matrix’’ for RP-PCA $M _ { \mathrm { R P - P C A } }$ is defined as 

$$
M _ {\mathrm{RP-PCA}} = \left( \begin{array}{c c} \Sigma_ {F} + c \sigma_ {e} ^ {2} & \Sigma_ {F} ^ {1 / 2} \mu_ {F} (1 + \tilde {\gamma}) \\ \mu_ {F} ^ {\top} \Sigma_ {F} ^ {1 / 2} (1 + \tilde {\gamma}) & (1 + \gamma) (\mu_ {F} ^ {\top} \mu_ {F} + c \sigma_ {e} ^ {2}) \end{array} \right).
$$

We define $\tilde { \gamma } ~ = ~ \sqrt { \gamma + 1 } - 1$ and note that $( 1 + \tilde { \gamma } ) ^ { 2 } = 1 + \gamma$ . The RP-PCA ‘‘signals’’ are the K largest eigenvalues $\theta _ { 1 } ^ { \mathrm { R P - P C A } } , \dotsc , \theta _ { K } ^ { \mathrm { R P - P C A } }$ of $M _ { \mathrm { R P - P C A } }$ . Intuitively, the signal of the factors is driven by $\Sigma _ { F } + ( 1 + \gamma ) \mu _ { F } \mu _ { F } ^ { \top }$ , which has the same K 

largest eigenvalues as19 

$$
\left( \begin{array}{c c} \Sigma_ {F} & \Sigma_ {F} ^ {1 / 2} \mu_ {F} (1 + \tilde {\gamma}) \\ \mu_ {F} ^ {\top} \Sigma_ {F} ^ {1 / 2} (1 + \tilde {\gamma}) & (1 + \gamma) (\mu_ {F} ^ {\top} \mu_ {F}) \end{array} \right).
$$

This is disturbed by the average noise which adds the matrix $\begin{array} { r l } {  { ( \begin{array} { c c } { c \sigma _ { e } ^ { 2 } I _ { K } } & { 0 } \\ { 0 } & { ( 1 + \gamma ) c \sigma _ { e } ^ { 2 } } \end{array} ) } } \end{array}$ Note that the disturbance also depends on the parameter γ . The eigenvalues of $M _ { \mathrm { R P - P C A } }$ are strictly larger than those of $M _ { \mathrm { P C A } } ,$ , if $\mu _ { F } \neq 0 .$ . Hence, RP-PCA has a stronger signal from its systematic component than PCA. We denote the corresponding orthonormal eigenvectors of $M _ { \mathrm { R P - P C A } }$ by U˜ : 

$$
\tilde {U} ^ {\top} M _ {\mathrm{RP-PCA}} \tilde {U} = \left( \begin{array}{c c c} \theta_ {1} ^ {\mathrm{RP-PCA}} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & \theta_ {K + 1} ^ {\mathrm{RP-PCA}} \end{array} \right).
$$

Unlike the conventional case of the covariance matrix with uncorrelated factors, we cannot link the eigenvalues of $M _ { \mathrm { R P - P C A } }$ with specific factors. The rotation U˜ tells us how much the first eigenvalue contributes to the first K factors, etc. We first derive the results for the special case $\Sigma = \sigma _ { e } ^ { 2 } I _ { N }$ before we treat the case of a general residual covariance matrix. 

Theorem 2 (Risk-Premium PCA Under Weak Factor Model). Assume Assumption 2 holds and $\scriptstyle { \mathcal { Z } } \ = \ \sigma _ { e } ^ { 2 } I _ { N }$ . We denote by $\theta _ { 1 } , \ldots , \theta _ { K }$ the first K largest eigenvalues of the signal matrix $M = M _ { P C A } \ o r \ M \ = \ M _ { R P - P C A }$ . The first K largest eigenvalues $\begin{array} { r } { \hat { \theta } _ { i } i = 1 , \dots , K o f \frac { 1 } { T } X ^ { \top } \left( I _ { T } + \gamma \frac { \mathbb { 1 } \mathbb { 1 } ^ { \top } } { T } \right) X } \end{array}$ satisfy 

$$
\hat {\theta} _ {i} \stackrel {{p}} {{\to}} \left\{ \begin{array}{l l} G ^ {- 1} \left(\frac {1}{\theta_ {i}}\right) & \text { if } \theta_ {i} > \theta_ {c r i t} = \lim _ {z \downarrow b} \frac {1}{G (z)} \\ b & \text { otherwise. } \end{array} \right.
$$

Define the correlation of the estimated with the population factors as 

$$
\widehat {C o r r} (F, \hat {F}) = d i a g \left(\frac {1}{T} F ^ {\top} \left(I - \frac {\mathbb {1 1} ^ {\top}}{T}\right) F\right) ^ {- 1 / 2} \left(\frac {1}{T} F ^ {\top} \left(I - \frac {\mathbb {1 1} ^ {\top}}{T}\right) \hat {F}\right) d i a g \left(\frac {1}{T} \hat {F} ^ {\top} \left(I - \frac {\mathbb {1 1} ^ {\top}}{T}\right) \hat {F}\right) ^ {- 1 / 2},
$$

which converges to 

$$
\widehat {C o r r} (F, \hat {F}) \stackrel {{p}} {{\to}} Q \left( \begin{array}{c c c c} \rho_ {1} & 0 & \dots & 0 \\ 0 & \rho_ {2} & \dots & 0 \\ 0 & 0 & \ddots & \vdots \\ 0 & \dots & 0 & \rho_ {K} \end{array} \right) R
$$

with 

$$
\rho_ {i} ^ {2} = \left\{ \begin{array}{l l} \frac {1}{1 + \theta_ {i} B \left(G ^ {- 1} \left(\frac {1}{\theta_ {i}}\right)\right)} & \text { if } \theta_ {i} > \theta_ {\text { crit }} \\ 0 & \text { otherwise. } \end{array} \right.
$$

If $\mu _ { F } \neq 0 ,$ , then for any $\gamma > - 1 R P { - } P C A$ strictly dominates PCA in terms of detecting factors, i.e. ρ can be positive for RP-PCA when it is zero for PCA (but not the other way around).20 

The two matrices Q and R are sub-matrices of rotation matrices and satisfy $Q ^ { \top } Q \leq I _ { K }$ and $R ^ { \top } R \leq I _ { K }$ . Hence, the correlation $\widehat { C o r r } ( F _ { i } , \hat { F } _ { i } )$ is not necessarily an increasing function in θ . For $\gamma > - 1$ the matrices equal: 

$$
Q = \left( \begin{array}{c c} I _ {K} & 0 \end{array} \right) \tilde {U} _ {1: K} \qquad R = D _ {K} ^ {1 / 2} d i a g (\Sigma_ {\hat {F}}) ^ {- 1 / 2},
$$

where $\tilde { U } _ { 1 : K }$ are the first K columns of $\tilde { U }$ and 

$$
\Sigma_ {\hat {F}} = D _ {K} ^ {1 / 2} \left(\left( \begin{array}{c c c} \rho_ {1} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & \rho_ {K} \\ 0 & \dots & 0 \end{array} \right) ^ {\top} \tilde {U} ^ {\top} \left( \begin{array}{c c} I _ {K} & 0 \\ 0 & 0 \end{array} \right) \tilde {U} \left( \begin{array}{c c c} \rho_ {1} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & \rho_ {K} \\ 0 & \dots & 0 \end{array} \right) + \left( \begin{array}{c c c} 1 - \rho_ {1} ^ {2} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & 1 - \rho_ {K} ^ {2} \end{array} \right)\right) D _ {K} ^ {1 / 2}
$$

$\hat { D } _ { K } = d i a g \left( \left( \hat { \theta } _ { 1 } \quad \cdot \cdot \cdot \quad \hat { \theta } _ { K } \right) \right)$ and $D _ { K }$ is the probability limit of $\hat { D } _ { K }$ . 

For PCA $( \gamma = - 1 )$ the two matrices simplify to $Q = R = I _ { K }$ . 

Theorem 2 states that the asymptotic behavior of the estimator can be explained by the signals of the factors for a given distribution of the idiosyncratic shocks. The theorem also states that weak factors can only be estimated with a bias. If a factor is too weak, then it cannot be detected at all. Weak factors can always be better detected using Risk-Premium-PCA instead of covariance PCA. The phase transition phenomena that hides weak factors can be avoided by putting some weight on the information captured by the risk-premium. Based on our asymptotic theory, we can choose the optimal weight $\gamma$ depending on our objective, e.g. to make all weak factors detectable or achieving the largest correlation for a specific factor. Typically the values in the matrices Q and R are decreasing in $\gamma$ while $\rho _ { i }$ is increasing in $\gamma ,$ , yielding an optimal value for the largest correlation. 

Theorem 2 assumes the special case of i.i.d. residuals with covariance matrix $\varSigma = \sigma _ { e } ^ { 2 } I _ { N }$ as we need to deal with the expression 

$$
\frac {1}{N} \text { trace } \left(\Sigma \left(\lambda I _ {N} - \frac {1}{T} e ^ {\top} e\right) ^ {- 1}\right)
$$

which simplifies to $\sigma _ { e } ^ { 2 } G ( \lambda ) + o _ { p } ( 1 )$ for $\Sigma = \sigma _ { e } ^ { 2 } I _ { N }$ . This result is not true for general residual covariance matrices. However, we are able to provide very close upper and lower bounds for the limiting correlations using modified signal matrices. We denote by $\bar { \sigma } _ { m i n } ^ { 2 }$ and $\sigma _ { m a x } ^ { 2 }$ the smallest respectively largest eigenvalue of Σ. Then, it holds that 

$$
\sigma_ {m i n} ^ {2} G (\lambda) + o _ {p} (1) \leq \frac {1}{N} \text { trace } \left(\Sigma \left(\lambda I _ {N} - \frac {1}{T} e ^ {\top} e\right) ^ {- 1}\right) \leq \sigma_ {m a x} ^ {2} G (\lambda) + o _ {p} (1).
$$

It turns out that there exist tighter bounds for the upper and lower bounds. We define $\underline { { \sigma } } _ { e , G } ^ { 2 }$ to be the largest value and $\bar { \sigma } _ { e , G } ^ { 2 }$ the smallest value such that 

$$
\sigma_ {e, G} ^ {2} + o _ {p} (1) \leq \frac {\frac {1}{N} \operatorname{trace} \left(\Sigma \left(\lambda I _ {N} - \frac {1}{T} e ^ {\top} e\right) ^ {- 1}\right)}{\frac {1}{N} \operatorname{trace} \left(\left(\lambda I _ {N} - \frac {1}{T} e ^ {\top} e\right) ^ {- 1}\right)} \leq \bar {\sigma} _ {e, G} ^ {2} + o _ {p} (1) \quad \text {   for   all   } \lambda \in (b, \infty).
$$

There exists a solution with $\sigma _ { m i n } ^ { 2 } \leq \underline { { { \sigma } } } _ { e , G } ^ { 2 } \leq \bar { \sigma } _ { e , G } ^ { 2 } \leq \sigma _ { m a x } ^ { 2 } ,$ , which can be obtained numerically from the above inequality. The same problem arises with the function B(λ). We define by $\underline { { \sigma } } _ { e , B } ^ { 2 }$ and $\bar { \sigma } _ { e , B } ^ { 2 }$ the largest respectively smallest value that satisfies 

$$
\sigma_ {e, B} ^ {2} + o _ {p} (1) \leq \frac {\frac {1}{N} \operatorname{trace} \left(\Sigma e ^ {\top} \left(\lambda I _ {T} - \frac {1}{T} e e ^ {\top}\right) ^ {- 2} e\right)}{\frac {1}{N} \operatorname{trace} \left(e ^ {\top} \left(\lambda I _ {T} - \frac {1}{T} e e ^ {\top}\right) ^ {- 2} e\right)} \leq \bar {\sigma} _ {e, B} ^ {2} + o _ {p} (1) \quad \text {   for   all   } \lambda \in (b, \infty).
$$

As before the solution exists with $\sigma _ { m i n } ^ { 2 } \leq \underline { { { \sigma } } } _ { e , B } ^ { 2 } \leq \bar { \sigma } _ { e , B } ^ { 2 } \leq \sigma _ { m a x } ^ { 2 }$ and can easily be calculated numerically. 

Based on the four different ‘‘noise variances’’ we introduce the corresponding signal matrices $M _ { \mathrm { R P - P C A } , G } , M _ { \mathrm { R P - P C A } , G }$ , $M _ { \mathrm { R P - P C A } , B }$ and $\bar { M } _ { \mathrm { R P - P C A } , B }$ which are defined analogously to $M _ { \mathrm { R P - P C A } }$ but replace $\sigma _ { e } ^ { 2 }$ by the different variance bounds; i.e. for example 

$$
\underline {{M}} _ {\text {RP - PCA}, G} = \left( \begin{array}{c c} \Sigma_ {F} & \Sigma_ {F} ^ {1 / 2} \mu_ {F} (1 + \tilde {\gamma}) \\ \mu_ {F} ^ {\top} \Sigma_ {F} ^ {1 / 2} (1 + \tilde {\gamma}) & (1 + \gamma) (\mu_ {F} ^ {\top} \mu_ {F}) \end{array} \right) + \underline {{\sigma}} _ {e, G} ^ {2} \cdot c \left( \begin{array}{c c} I _ {K} & 0 \\ 0 & (1 + \gamma) \end{array} \right).
$$

The eigenvalues of these signal matrices are the signals $\underline { { \theta } } _ { i , G } , \bar { \theta } _ { i , G } , \underline { { \theta } } _ { i , B }$ and $\bar { \theta } _ { i , B }$ with the corresponding eigenvectors $\underline { { U } } _ { G } , \bar { U } _ { G } , \underline { { U } } _ { B }$ and $\boldsymbol { \bar { U } } _ { B }$ , i.e. for example 

$$
\underline {{U}} _ {G} ^ {\top}   \underline {{M}} _ {\text { RP - PCA, G }}   \underline {{U}} _ {G} = \left( \begin{array}{c c c} \underline {{\theta}} _ {1, G} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & \underline {{\theta}} _ {K + 1, G} \end{array} \right).
$$

Theorem 3 (Risk-Premium PCA Under Weak Factor Model for General Residual Covariance Matrix). Assume Assumption 2 holds. The first K largest eigenvalues $\begin{array} { r } { \hat { \theta } _ { i } i = 1 , \dots , K o f \frac { 1 } { T } X ^ { \top } \left( I _ { T } + \gamma \frac { \mathbb { 1 } \mathbb { 1 } ^ { \top } } { T } \right) } \end{array}$ X satisfy 

$$
\underline {{\theta}} _ {i} \leq \hat {\theta} _ {i} + o _ {p} (1) \leq \bar {\theta} _ {i}
$$

with 

$$
\underline {{\theta}} _ {i} = \left\{ \begin{array}{l l} G ^ {- 1} \left(\frac {1}{\underline {{\theta}} _ {i , G}}\right) & i f \underline {{\theta}} _ {i, G} > \theta_ {c r i t} = \lim _ {z \downarrow b} \frac {1}{G (z)} \\ b & o t h e r w i s e. \end{array} \right.
$$

$$
\bar {\theta} _ {i} = \left\{ \begin{array}{l l} G ^ {- 1} \left(\frac {1}{\bar {\theta} _ {i , G}}\right) & \text { if   } \bar {\theta} _ {i, G} > \theta_ {c r i t} \\ b & \text { otherwise. } \end{array} \right.
$$

The correlation of the estimated with the true factors converges to 

$$
\widehat {C o r r} (F, \hat {F}) \xrightarrow {p} \tilde {Q} \left( \begin{array}{c c c c} \tilde {\rho} _ {1} & 0 & \dots & 0 \\ 0 & \tilde {\rho} _ {2} & \dots & 0 \\ 0 & 0 & \ddots & \vdots \\ 0 & \dots & 0 & \tilde {\rho} _ {K} \end{array} \right) \tilde {R}
$$

with 

$$
\tilde {Q} = \left( \begin{array}{c c} I _ {K} & 0 _ {K \times 1} \end{array} \right) V
$$

$$
\tilde {R} = \text {diag} \left(I _ {K} - \left( \begin{array}{c c c c} \tilde {\rho} _ {1} & 0 & \dots & 0 \\ 0 & \tilde {\rho} _ {2} & \dots & 0 \\ 0 & 0 & \ddots & \vdots \\ 0 & \dots & 0 & \tilde {\rho} _ {K} \end{array} \right) V ^ {\top} \left( \begin{array}{c c} 0 _ {K \times K} & 0 _ {K \times 1} \\ 0 _ {1 \times K} & 1 \end{array} \right) V \left( \begin{array}{c c c c} \tilde {\rho} _ {1} & 0 & \dots & 0 \\ 0 & \tilde {\rho} _ {2} & \dots & 0 \\ 0 & 0 & \ddots & \vdots \\ 0 & \dots & 0 & \tilde {\rho} _ {K} \end{array} \right)\right) ^ {- 1 / 2}
$$

and $V _ { i } f o r i = 1 , \dots , K$ are the solutions to 

$$
\left(I _ {K + 1} - \left(\left( \begin{array}{c c} \Sigma_ {F} & \Sigma_ {F} ^ {1 / 2} \mu_ {F} (1 + \tilde {\gamma}) \\ \mu_ {F} ^ {\top} \Sigma_ {F} ^ {1 / 2} (1 + \tilde {\gamma}) & (1 + \gamma) (\mu_ {F} ^ {\top} \mu_ {F}) \end{array} \right) G (\hat {\theta} _ {i}) + \left( \begin{array}{c c} I _ {K} & 0 \\ 0 & (1 + \gamma) \end{array} \right) c \cdot \tilde {G} (\hat {\theta} _ {i})\right)\right) V _ {i} = o _ {p} (1)
$$

for $i = 1 , \ldots , K$ with $\frac { 1 } { N }$ trace $\begin{array} { r } { \bigg ( \Sigma ( \lambda I _ { N } - \frac { 1 } { T } e ^ { \top } e ) ^ { - 1 } \bigg ) \stackrel { p } {  } \tilde { G } ( \lambda ) } \end{array}$ . The correlation is bounded asymptotically from below and above by 

$$
\overline {{C o r r}} (F, \hat {F}) = \tilde {Q} \left( \begin{array}{c c c c} \bar {\rho} _ {1} & 0 & \dots & 0 \\ 0 & \bar {\rho} _ {2} & \dots & 0 \\ 0 & 0 & \ddots & \vdots \\ 0 & \dots & 0 & \bar {\rho} _ {K} \end{array} \right) \bar {R}, \qquad \underline {{C o r r}} (F, \hat {F}) = \tilde {Q} \left( \begin{array}{c c c c} \underline {{\rho}} _ {1} & 0 & \dots & 0 \\ \underline {{0}} & \underline {{\rho}} _ {2} & \dots & 0 \\ 0 & 0 & \ddots & \vdots \\ 0 & \dots & 0 & \underline {{\rho}} _ {K} \end{array} \right) \underline {{R}}.
$$

with $\underline { { \rho } } _ { i } \le \tilde { \rho } _ { i } \le \bar { \rho } _ { i }$ and $\underline { { R } } \leq \tilde { R } \leq \bar { R } :$ 

$$
\underline {{\rho}} _ {i} ^ {2} = \left\{ \begin{array}{l l} \frac {1}{1 + \bar {\theta} _ {i , B} B \Big (G ^ {- 1} \Big (\frac {1}{\bar {\theta} _ {i , G}} \Big) \Big)} & \text {if} \underline {{\theta}} _ {i, G} > \theta_ {c r i t} \\ 0 & \text {otherwise} \end{array} \right. \quad \bar {\rho} _ {i} ^ {2} = \left\{ \begin{array}{l l} \frac {1}{1 + \underline {{\theta}} _ {i , B} B \Big (G ^ {- 1} \Big (\frac {1}{\bar {\theta} _ {i , G}} \Big) \Big)} & \text {if} \bar {\theta} _ {i, G} > \theta_ {c r i t} \\ 0 & \text {otherwise}. \end{array} \right.
$$

$$
\underline {{R}} = \text { diag } \left(I _ {K} - \left( \begin{array}{c c c c} \underline {{\rho}} _ {1} & 0 & \dots & 0 \\ 0 & \underline {{\rho}} _ {2} & \dots & 0 \\ 0 & 0 & \ddots & \vdots \\ 0 & \dots & 0 & \underline {{\rho}} _ {K} \end{array} \right) V ^ {\top} \left( \begin{array}{c c} 0 _ {K \times K} & 0 _ {K \times 1} \\ 0 _ {1 \times K} & 1 \end{array} \right) V \left( \begin{array}{c c c c} \underline {{\rho}} _ {1} & 0 & \dots & 0 \\ 0 & \underline {{\rho}} _ {2} & \dots & 0 \\ 0 & 0 & \ddots & \vdots \\ 0 & \dots & 0 & \underline {{\rho}} _ {K} \end{array} \right)\right) ^ {- 1 / 2}
$$

and ansignals sly foand $\bar { \rho } _ { i \cdot } I f \mu _ { F } \neq 0 ,$ $\gamma > - 1 R P - P C A$ has strictly simplify to and upper bounds for theand the lower and upper $\underline { { \theta } } _ { i , G } ^ { R \vdash R C A }$ $\bar { \theta } _ { i , G } ^ { R P - P C A }$ $( \gamma = - 1 )$ $\tilde { \boldsymbol { Q } } = \tilde { \boldsymbol { R } } = \boldsymbol { I } _ { K }$ $\underline { { \theta } } _ { i , G } = \bar { \theta } _ { i , G }$ ${ \underline { { \rho } } } _ { i } = { \bar { \rho } } _ { i }$ 

The takeaways from the simple residual covariance case carry over to a general residual covariance case. The correlation of the estimated factors with the population factors depends on the signals of the factors which is strengthened for RP-PCA. The formulas for the lower and upper bounds of the eigenvalues and correlations are analogous to the simple covariance case but use a modified signal matrix. Simulations show that these bounds are very tight. The upper bound for the correlation of PCA factors can be smaller than the lower bound for RP-PCA factors. In particular, the PCA upper bound can be zero while the RP-PCA lower bound is positive, in which case the phase transition phenomena hides the weak PCA factors which are detected by RP-PCA. 

# 5.3. Example

In order to obtain a better intuition for the problem we consider the special case of only one factor with crosssectionally uncorrelated residuals. 

Example 2 (One-factor Model with i.i.d. Residuals). Assume that there is only one factor, i.e. $K = 1$ . We introduce the following notation 

• Noise-to-signal ratio: $\begin{array} { r } { \varGamma _ { e } = \frac { c { \cdot } \sigma _ { e } ^ { 2 } } { \sigma _ { F } ^ { 2 } } } \end{array}$ σ 2 

• Sharpe-ratio: $\begin{array} { r } { S R = \frac { \mu _ { F } } { \sigma _ { F } } } \end{array}$ . 

• $\psi ( \theta _ { 1 } ) : = B ( \hat { \theta } _ { 1 } ( \theta _ { 1 } ) ) = B \left( G ^ { - 1 } ( 1 / \theta _ { 1 } ) \right)$ . 

The signal matrix $M _ { R P - P C A }$ simplifies to 

$$
M _ {\text { RP - PCA }} = \sigma_ {F} ^ {2} \left( \begin{array}{c c} 1 + \Gamma_ {e} & S R \sqrt {1 + \gamma} \\ S R \sqrt {1 + \gamma} & (S R ^ {2} + \Gamma_ {e}) (1 + \gamma) \end{array} \right)
$$

and has the largest eigenvalue: 

$$
\theta_ {1} = \frac {1}{2} \sigma_ {F} ^ {2} \left(1 + \Gamma_ {e} + (S R ^ {2} + \Gamma_ {e}) (1 + \gamma) + \sqrt {(1 + \Gamma_ {e} + (S R ^ {2} + \Gamma_ {e}) (1 + \gamma)) ^ {2} - 4 (1 + \gamma) \Gamma_ {e} (1 + S R ^ {2} + \Gamma_ {e})}\right).
$$

Corollary 2 (One-factor Model with i.i.d. Residuals). Assume Assumption 2 holds, K = 1 and $e _ { t , i }$ i.i.d. $N ( 0 , \sigma _ { e } ^ { 2 } )$ ). The correlation between the estimated and true factor has the following limit: 

$$
\widehat {C o r r} (F, \hat {F}) ^ {2} \stackrel {{p}} {{\to}} \frac {1}{1 + \theta \Psi (\theta) \left(\frac {\left(\frac {\theta}{\sigma_ {F} ^ {2}} - (1 + \Gamma_ {e})\right) ^ {2}}{S R ^ {2} (1 + \gamma)} + 1\right)}
$$

and the estimated Sharpe-ratio converges to 

$$
\widehat {S R} := \frac {\frac {1}{T} \sum_ {t = 1} ^ {T} \hat {F}}{\left(\frac {1}{T} \hat {F} ^ {\top} \left(I - \frac {\mathbb {1 1} ^ {\top}}{T}\right) \hat {F}\right) ^ {1 / 2}} \xrightarrow {p} \frac {\frac {\theta}{\sigma_ {F} ^ {2}} - (1 + \Gamma_ {e})}{S R (1 + \gamma)} \widehat {C o r r} (F, \hat {F}).
$$

For $\gamma \to \infty$ these limits converge to 

$$
\widehat {C o r r} (F, \hat {F}) ^ {2} \xrightarrow {p} \frac {1}{1 + \Gamma_ {e} + \frac {\Gamma_ {e} ^ {2}}{S R ^ {2}}}
$$

$$
\widehat {S R} \xrightarrow {p} \left(S R + \frac {\Gamma_ {e}}{S R}\right) \frac {1}{\sqrt {1 + \Gamma_ {e} + \frac {\Gamma_ {e} ^ {2}}{S R ^ {2}}}}.
$$

In the case of PCA, i.e. γ = −1 the expression simplifies to 

$$
\widehat {C o r r} (F, \hat {F}) ^ {2} \xrightarrow {p} \frac {1}{1 + \theta \Psi (\theta)}
$$

with $\theta _ { P C A } = \sigma _ { F } ^ { 2 } ( 1 + { \cal { T } } _ { e } ) .$ . The function G(.) and $B ( . )$ are given in closed form. The Cauchy transform takes the form 

$$
G (z) = \frac {z - \sigma_ {e} ^ {2} (1 - c) - \sqrt {(z - \sigma_ {e} ^ {2} (1 + c)) ^ {2} - 4 c \sigma_ {e} ^ {2}}}{2 c z \sigma_ {e} ^ {2}}.
$$

The maximum residual eigenvalue converges to√ $b = \sigma _ { e } ^ { 2 } ( 1 + \sqrt { c } ) ^ { 2 } $ . Hence, the critical value for detecting factors is $\theta _ { c r i t } =$ $\begin{array} { r } { \frac { 1 } { G ( b ^ { + } ) } = \sigma _ { e } ^ { 2 } ( c + \sqrt { c } ) } \end{array}$ . The inverse of the Cauchy transform and the B-function are given explicitly by 

$$
G ^ {- 1} \left(\frac {1}{z}\right) = z \left(\frac {1 + \frac {\sigma_ {e} ^ {2} (1 - c)}{z}}{1 - \frac {c \sigma_ {e} ^ {2}}{z}}\right)
$$

$$
B (z) = \frac {z - \sigma_ {e} ^ {2} (1 + c)}{2 \sigma_ {e} ^ {2} \sqrt {z ^ {2} - 2 (1 + c) \sigma_ {e} ^ {2} z + (c - 1) ^ {2} \sigma_ {e} ^ {4}}} - \frac {1}{2 \sigma_ {e} ^ {2}}.
$$

For the PCA case, i.e. $\gamma = - 1 ,$ , the largest eigenvalue of the sample covariance matrix converges $t o ^ { 2 1 }$ : 

$$
\hat {\theta} _ {1} \stackrel {{p}} {{\to}} \left\{ \begin{array}{l l} \sigma_ {F} ^ {2} + \frac {\sigma_ {e} ^ {2}}{\sigma_ {F} ^ {2}} (c + 1 + \sigma_ {e} ^ {2}) & i f \sigma_ {F} ^ {2} + c \sigma_ {e} ^ {2} > \theta_ {c r i t} \Leftrightarrow \sigma_ {F} ^ {2} > \sqrt {c} \sigma_ {e} ^ {2} \\ \sigma_ {e} ^ {2} (1 + \sqrt {c}) ^ {2} & o t h e r w i s e. \end{array} \right.
$$

and the correlation between the estimated and true factor converges to $\rho _ { 1 }$ : 

$$
\rho_ {1} ^ {2} = \left\{ \begin{array}{l l} \frac {1 - \frac {c \sigma_ {e} ^ {4}}{\sigma_ {F} ^ {4}}}{1 + \frac {c \sigma_ {e} ^ {2}}{\sigma_ {F} ^ {2}} + \frac {\sigma_ {e} ^ {4}}{\sigma_ {F} ^ {4}} (c ^ {2} - c)} & \text {if} \sigma_ {F} ^ {2} + c \sigma_ {e} ^ {2} > \theta_ {\text {crit}} \\ 0 & \text {otherwise.} \end{array} \right.
$$

A smaller noise-to-signal ratio $\varGamma _ { e }$ and a larger Sharpe-ratio combined with a large γ lead to a more precise estimation $\frac { \left( \frac { \theta } { \sigma _ { F } ^ { 2 } } - ( 1 + { r _ { e } } ) \right) ^ { 2 } } { S R ^ { 2 } ( 1 + \gamma ) }$ 2 of the factors. Note that a larger value of γ decreases $\theta \psi ( \theta )$ , while it increases , creating a trade-off. In the simulation section we analyze this trade-off and find the optimal value of $\gamma$ to maximize the correlation. In all our simulations $\gamma = - 1$ was never optimal. Note, that for the factor variance $\sigma _ { F } ^ { 2 }$ going to infinity, we are back in the strong factor model and the estimator becomes consistent.22 

# 6. Simulation

Next, we illustrate the performance of RP-PCA and its ability to detect weak factors with high Sharpe-ratios using a simulation exercise. We simulate factor models that try to replicate moments of the data that we are going to study in Section 7. The parameters of the factors and idiosyncratic components are based on our empirical estimates. We analyze the performance of RP-PCA for different values of $\gamma ,$ , sample size and strength of the factors. Conventional PCA corresponds to $\gamma = - 1$ . In a factor model only the product $F A ^ { \top }$ is well-identified and the strength of the factors could be either modeled through the moments of the factors or the values of the loadings. Throughout this section we normalize the loadings to $\boldsymbol { A } ^ { \top } \boldsymbol { A } / N \stackrel { p } {  } \boldsymbol { I } _ { K }$ and vary the moments of the factors. The factors are uncorrelated with each others and have different means and variances. The variance of the factor can be interpreted as the proportion of assets affected by this factor. With this normalization a factor with a variance of $\sigma _ { F } ^ { 2 } = 0 . 5$ could be interpreted as affecting 50% of the assets with an average loading strength of 1. The theoretical results for the weak factor model are formulated under the normalization $A ^ { \top } A \stackrel { p } {  } I _ { K }$ . The PCA signal in the weak factor framework corresponds to $\sigma _ { F } ^ { 2 }$ · N under the normalization in the simulation.23 

The strength of a factor has to be put into relation to the noise level. Based on our theoretical results the signal to noise ratio $\frac { \sigma _ { F } ^ { 2 } } { \sigma _ { e } ^ { 2 } }$ with $\begin{array} { r } { \sigma _ { e } ^ { 2 } = \frac { 1 } { N } \sum _ { i = 1 } ^ { N } \sigma _ { e , i } ^ { 2 } } \end{array}$ determines the variance signal of $\mathsf { a f a c t o r . } ^ { 2 4 }$ Our empirical results suggest a signal eto noise ratio of around 5–8 for the first factor which is essentially a market factor. The remaining factors in the different data sets seem to have a variance signal between 0.04 and 0.8. Based on this insight we will model a four-factor model with variances $\Sigma _ { F } = \mathrm { d i a g } ( 5 , 0 . 3 , 0 . \bar { 1 } , \sigma _ { F } ^ { 2 } )$ . The variance of the fourth factor takes the values $\sigma _ { F } ^ { 2 } \in \{ 0 . 0 3 , 0 . 1 \}$ . The first factor is a dominant market factor, while the second is also a strong factor. The third factor is weak, while the fourth factor varies from very weak to weak. We normalize the factors to be uncorrelated with each other. The Sharpe-ratios are defined as $S R _ { F } = ( 0 . 1 2 , 0 . 1 , 0 . 3 , s r )$ , where the Sharpe-ratio of the fourth factor varies between the following values $s r \in \{ 0 . 2 , 0 . 3 , 0 . 5 , 0 . 8 \}$ . These parameter values are consistent with our data sets. 

The properties of the estimation approach depend on the average idiosyncratic variance and dependency structure in the residuals. We normalize the average noise variance $\sigma _ { e } ^ { 2 } = 1$ , which implies that the factor variances can be directly compared to the variance signals in the data.25 We use two different sets of residual correlation matrices. 

First, the correlation matrix of our simulated residuals is set to the empirical correlation that we observe in the data. In more detail, we have estimated the residual correlation matrix based on $N = 2 5$ size and value double-sorted portfolios, $N = 7 4$ extreme deciles sorted portfolios and $N = 3 7 0$ decile sorted portfolios as described in the empirical Section $7 . ^ { 2 6 }$ In each case we have first regressed out the systematic factors and then estimated the residual covariance matrix with a hard thresholding approach setting small values to zero.27 This provides a consistent estimator of the residual population covariance matrix. We have regressed out the first 3 PCA factors for the first data set and the first 6 PCA factors for the last two data $\mathsf { s e t s } . ^ { 2 8 }$ The remaining correlation structure in the residuals is sparse. In particular the estimated eigenvalues of the simulated residuals coincide with the empirical estimates of the eigenvalues. Second, for $N = 3 7 0$ assets we create a sparse residual correlation matrix based on $\Sigma { = } C C ^ { \top }$ , where C is a matrix where the first 13 off-diagonal elements take the value 0.7. The resulting covariance matrix is normalized to the corresponding correlation matrix. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/f275355c0afeab6048a823491ca4c55f4d3f50d9af057b22f14fb9a9bdc75ede.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/2a8c40c61b74407a61463e8db502cd633793c638dcac9101622c275a2f2d0935.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/c28ce7f4caa2c0330f698503711c4b7e3035fb6e36f79348a546d292de5063f5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/ab41adbb6ade49db6716c4e4e0b5f9d52b77268d627b5af853c95b5a5cfa6286.jpg)



Fig. 1. Sample paths of the cumulative returns of the first four factors and the estimated factor processes. The fourth factor has a variance $\sigma _ { F } ^ { 2 } = 0 . 0 3$ and Sharpe-ratio sr = 0.5. N = 370 and T = 650.


In the main part we consider only the cross-sectional dimension $N = 3 7 0$ and time dimension $T \ : = \ : 6 5 0$ for the empirical residual correlation matrix. The Appendix includes the results for the block-diagonal residual correlation matrix. In the online appendix we also study the combinations $\{ N = 7 4 , T = 6 5 0 \}$ and $\{ N = 2 5 , T = 2 4 0 \}$ motivated by our empirical analysis and include results for the pricing errors. 

The loadings are i.i.d draws from a standard multivariate normal distribution. The factors are i.i.d. draws from a multivariate normal distribution with means and variances specified as above. The idiosyncratic components are i.i.d. draws from a multivariate normal distribution with mean zero and covariance matrix based on a consistent estimation of the empirical residual correlation matrix respectively the parametric band-diagonal matrix.29 For each setup we run 100 Monte-Carlo simulations. For the out-of-sample results we first estimate the loading vector in-sample and then obtain the out-of-sample factor estimates by projecting the out-of-sample returns on the estimated loadings. 

Fig. 1 provides some intuition for our estimator. It illustrates the sample path estimates for different values of $\gamma$ . If the fourth factor is weak with a high Sharpe-ratio, then conventional PCA or RP-PCA with a too small value of $\gamma$ cannot detect it, while RP-PCA with a sufficiently large γ is able to detect the factor. 

Figs. 2 and 3 show correlations and Sharpe-ratios in the four-factor model for $N = 3 7 0$ and $T = 6 5 0$ based on the empirical residual correlation structure. The risk-premium weight γ has the largest effect on estimating the fourth factor if it is weak $( \sigma _ { F } ^ { 2 } = 0 . 0 3 )$ and has a high Sharpe ratio $( s r \ge 0 . 3 )$ . The second takeaway is that the estimates of the strong factors are essentially not affected by the properties of the weak factors and vice versa. Hence, one could first estimate the strong factors and project them out and then estimate the weak factors from the projected data. Motivated by this finding we will study a one-factor model in more detail and compare the prediction of our weak factor model with Monte-Carlo simulations. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/a14446cadbc16ef5e5dc4df0d035448ce9f4adbfefebdfb8fca195cab601cf4e.jpg)



Fig. 2. $N = 3 7 0 , T = 6 5 0 ;$ : Correlation of estimated rotated factors in-sample and out-of-sample for different variances and Sharpe-ratios of the fourth factor and for different RP-weights γ . We use the empirical residual correlation matrix.


In Figs. 4 and A.11 we first calculate the lower and upper bounds for the correlation between estimated and population factors based on the weak factor model in Theorem 3. We also include the parameter $\rho$ which drives the correlation. Although the residual covariance matrix takes a general form here, we also include the predicted correlation based on Theorem 2. In this case, which we label as the ‘‘exact’’ model, the signal matrix is based on $\scriptstyle { \frac { 1 } { N } } \mathrm { t r a c e } ( \Sigma )$ which corresponds to an average noise level while the upper and lower bounds are based on a lower respectively higher noise variance. Hence, the exact model is assumed to take values between the lower and upper bound which is exactly what we observe. In fact, the bounds are very tight, in particular for higher Sharpe-ratios or variance signals. Hence, for the following simulations we will only report the exact results based on Theorem 2. 

Figs. 5 and A.10 compare the prediction of our weak factor model theory with a Monte-Carlo simulation for the empirical and the band-diagonal residual correlation matrix. We consider a factor variance $\sigma _ { F } ^ { 2 } \in \{ 0 . 0 3 , 0 . 1 \}$ . The Supplementary Appendix collects the results for a wider range of values. The risk-premium weight $\gamma$ has the largest effect on correlations, Sharpe-ratios and pricing errors if the factors are weak $( \sigma _ { F } ^ { 2 } = 0 . 0 3 )$ and have a high Sharpe ratio $( s r \ge 0 . 3 )$ . Note, that if there is not much information in the mean, i.e. the Sharpe-ratio of the factor is low, a too high value $\gamma > 1 0$ can lead to an overestimation of the Sharpe-ratio in-sample. This makes sense because if too much weight is given to an uninformative mean, the estimator will pick up some of the non-zero residuals. Note, that the out-of-sample results provide reliable estimates that are not affected by overfitting issues. 

Fig. 6 compares the prediction of our weak factor model theory with a Monte-Carlo simulation as a function of the variance signal. We consider one factor with Sharpe-ratio 0.8, but increasing variance. The prediction of our statistical model is confirmed by the Monte-Carlo simulation. It convincingly shows how weak factors can be better estimated with RP-PCA with a large $\gamma$ when the Sharpe-ratio is high. In Fig. 7 we plot the value of $\rho _ { i } ^ { 2 }$ in the weak factor model which determines the detection and correlation of the factors. We vary the signal θ which among others depends on the choice of $\gamma .$ . We compare uncorrelated residuals with our weak dependency structures. It is apparent that increasing the signal strength for detecting weak factors becomes more relevant for correlated residuals. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/76ea6e3994c15beafcffe2dc51298ed6862266a4ed61983a7285b1823f6426e8.jpg)



Fig. 3. N = 370, T = 650: Sharpe ratios of estimated rotated factors in-sample and out-of-sample for different variances and Sharpe-ratios of the fourth factor and for different RP-weights γ . We use the empirical residual correlation matrix.


The results for $N = 7 4$ and N = 25 are similar to the results for N = 370. Actually, our estimator has a larger effect for smaller values of N as this implies a weaker signal for the factors and hence RP-PCA can perform even better.30 

# 7. Empirical application

We apply our estimator to a large number of anomaly sorted portfolios. The same data is studied in more detail in our companion paper (Lettau and Pelger, 2020). Based on the universe of U.S. firms in CRSP, we consider 37 anomaly characteristics following standard definitions in Novy-Marx and Velikov (2016) and McLean and Pontiff (2016). We use the same data set as Kozak et al. $( 2 0 1 8 ) ^ { 3 1 }$ who have sorted the stock returns in yearly rebalanced decile portfolios. This gives us a total cross-section of $N = 3 7 0$ portfolios of monthly returns from 07/1963 to 12/2017 (T = 650).32 The risk-free rate to obtain excess returns is from Kenneth French’s website. We estimate statistical factors for different choices of γ and evaluate the maximum Sharpe-ratio, average pricing error and explained variation in- and out-of-sample. 

Table 1 reports the results for K = 3 and K = 5 factors for RP-PCA with γ = 10 and PCA (γ = −1). SR denotes the maximum Sharpe-ratio that can be obtained by a linear combination of the factors, i.e. it combines the factors with the weights $\mathop { \sum _ { F } } ^ { - 1 } \mu _ { F }$ . It measures how well the factors can approximate the stochastic discount factor. The root-mean-squared pricing error (RMSα) equals $\textstyle { \sqrt { { \frac { 1 } { N } } \sum _ { i = 1 } ^ { N } \alpha _ { i } ^ { 2 } } }$ , where the pricing error $\alpha _ { i }$ is the intercept of a time-series regression of the excess return of asset i on the factors. The idiosyncratic variation is the average variance of the residuals after regressing out the factors. The in-sample analysis is based on the whole time horizon of T = 650 months. The out-of-sample analysis estimates the loadings with a rolling window of 20 years (T = 240). With these estimated loadings including information 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/4464a038744447fbe3299a56e5f204b1d15edc000f4109efb4759038c6f0bc9d.jpg)



Fig. 4. $N = 3 7 0 , T = 6 5 0 ;$ Upper and lower bounds for the correlations and parameter ρ as a function of the RP-weight γ for different variances and Sharpe-ratios. The residuals have the empirical residual correlation matrix.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/c784d7466eeed514e6066441e7c5108f621ac4bf96824190057a14214a2d2f46.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/e532c26212bc9547d57af1140d5bbfcd1fe7775ae39d4aec48b30bdeda3f767b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/63e0f4bff0183ccbcf6aee9b23d2a05e6a2540228fcf75f99109643492ec1410.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/1a88650fa028c7d716c7a50e560ffed002345c0371296bdd7f64c69ae2a07974.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/ccd9605e5651ff58d3171cb99b5e553ae20d96816b93a2fe9da187c39954e516.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/d265e300a78727a7c33631e6d063113adf30da0504ae877a7b55f448d2d75875.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/049de55f9ba343bfb2c4eaf6366ec3b37f0ecfabdaa455c99e92a6d8a125f021.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/c56c3c6a8466d932d9a1b505dfbd867113229b9b2f2f7635b22b4e20e3fa6906.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/73f5b4a08e44895c0a866c8caa0911faeb45bd31168a2f0307392dd960afc37c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/c500c7ae223dffd3052a0b317985598570b83f506097b007da9fe83e754be5b6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/51f5151dfbd8c3c45bb819ae7fa1e763ed800b2c60a73502555be7395db6c50f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/d197722a1c77ecc8427d9a9f50a209a734e8a777a23ff240efce4519d7ed2127.jpg)



Fig. 5. $N = 3 7 0 , T = 6 5 0 ;$ Correlations and Sharpe-ratios as a function of the RP-weight $\gamma$ for different variances and Sharpe-ratios. The residuals have the empirical residual correlation matrix.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/623afc8bfe1d5bfc9ac2ebc8da7a567c1a4f82ccd336857e721c0ba9620ba946.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/e2fbecf6c270f81aee5bf91dce717da70ed501305456771588d4cbd21c362d5d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/2bd13b828b1a2dfb2ee7654477d362cb300d2061220a8e3b40bf2dcc71ecd4d5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/8086c8213496a8d40747374e21728b33321f2b3aca92e85722fc0777bcada313.jpg)



Fig. 6. Correlations between estimated and true factor based on the weak factor model prediction and Monte-Carlo simulations for different variances of the factor. Left plots: The residuals have cross-sectional correlation defined by the band-diagonal matrix. Right plots: The residuals have the empirical residual correlation matrix. The Sharpe-ratio of the factor is 0.8, i.e. the mean equals $\mu _ { F } = 0 . 8 \cdot \sigma _ { F }$ . We have $T = 6 5 0$ and $N = 3 7 0 ,$ , i.e. the normalized variance of the factors in the weak factor model corresponds to $\sigma _ { F } ^ { 2 } \cdot N .$ .


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/c4789671218f186dcf47c804e58540fc8e1fab8fc89bb54fdce9a53c8316f085.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/4f9827a6c073107d63567cef70bb0d6b13ddacdec3afb67cac61c3015fafc234.jpg)



Fig. 7. Model-implied values of $\begin{array} { r } { \rho _ { i } ^ { 2 } ~ = ~ \frac { 1 } { 1 + \theta _ { i } B ( \hat { \theta } _ { i } ) } ~ \mathrm { i f } ~ \theta _ { i } > \sigma _ { c r i t } ^ { 2 } } \end{array}$ and 0 otherwise) for different signals θi. The average noise level is normalized in both cases to $\sigma _ { e } ^ { 2 } = 1 .$ . Left plots: The residuals have cross-sectional correlation defined by the band-diagonal matrix. Right plots: The residuals have the empirical residual correlation matrix.


up to time t we predict the systematic return and obtain a pricing error out-of-sample at $t + 1$ . This corresponds to a cross-sectional pricing regression with out-of-sample loadings. The mean and variance of the out-of-sample errors are used to calculate the average pricing error and the idiosyncratic variation. We use the optimal portfolio weights for the maximum Sharpe-ratio portfolio estimated in the rolling window period to create an out-of-sample optimal return giving us the maximum Sharpe-ratio portfolio out-of-sample. 

RP-PCA and PCA differ the most in terms of the maximum Sharpe-ratio. For $K = 5$ factors the in- and out-of-sample Sharpe-ratio of RP-PCA is twice as large as for PCA. For K = 3 factors there is still a sizeable difference in Sharpe-ratios, but it is less pronounced than for a larger number of factors. A possible reason is that the 4th or 5th factor is weak with a high Sharpe-ratio and only picked up by RP-PCA, while the first four factors are stronger and hence can be detected by PCA. Surprisingly, the pricing errors and the unexplained variation are very close for the two methods. Only the outof-sample pricing error of RP-PCA is smaller than for PCA. It seems that RP-PCA selects high Sharpe-ratio factors with smaller out-of-sample pricing errors without sacrificing explanatory power for the variation. 

Fig. 8 analyzes the effect of $\gamma$ and the number of factors on the three criteria maximum Sharpe-ratio, pricing error and variation. The Sharpe-ratio and pricing error change significantly when including the 5th factor. This 5th factor is also strongly affected by the choice of $\gamma$ and seems to require $\gamma > 5$ to be detected by RP-PCA. Adding the 6th factor has only a very minor effect on the three criteria. That is why we opt for a 5-factor model.33 The figure illustrates that the amount of unexplained variation is insensitive to the choice of $\gamma .$ Hence, our factors capture more pricing information while explaining the same amount of variation in the data. 


Table 1 Deciles of 37 single-sorted portfolios from 07/1963 to 12/2016 (N = 370 and T = 650): Maximal Sharperatios, root-mean-squared pricing errors and idiosyncratic variation for different number of factors. RP-weight γ = 10.


<table><tr><td rowspan="2"></td><td colspan="3">In-sample</td><td colspan="3">Out-of-sample</td></tr><tr><td>SR</td><td>RMS α</td><td>Idio. Var.</td><td>SR</td><td>RMS α</td><td>Idio. Var.</td></tr><tr><td>RP-PCA 3 factors</td><td>0.23</td><td>0.17</td><td>12.75%</td><td>0.18</td><td>0.15</td><td>14.57%</td></tr><tr><td>PCA 3 factors</td><td>0.17</td><td>0.17</td><td>12.68%</td><td>0.14</td><td>0.15</td><td>14.66%</td></tr><tr><td>RP-PCA 5 factors</td><td>0.53</td><td>0.14</td><td>10.76%</td><td>0.45</td><td>0.12</td><td>12.70%</td></tr><tr><td>PCA 5 factors</td><td>0.24</td><td>0.14</td><td>10.66%</td><td>0.17</td><td>0.14</td><td>12.56%</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/b826d744726f1c464a85265a83a5f38e8fad67af1db1e71708026179711f576a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/68ca322a5b1474e607470ea119178074ca7ee804b637e7b918d273b979c8e9ab.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/8b26f21e2d7e6fde44a89ac770a32062df6121d110e83e45b6840adfc0fda2e7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/2ee885739d782b2678de5a4d3436174dcf2ddb35d5fefe909b5961b6a398ab10.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/8c34b88b78739a471388cbeeb70df6a44f24bcccad3bd40b98d41f4be7d27020.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/55ad5bf3ed65d8b2d1599bb551b165057c5e2b9b65e71c8974d662d1023965c2.jpg)



Fig. 8. Deciles of 37 single-sorted portfolios from 07/1963 to 12/2016 (N = 370 and T = 650): Maximal Sharpe-ratios, root-mean-squared pricing errors and unexplained idiosyncratic variation for different values of γ .


Table 2 shows that the variance signal for different factors suggests the existence of weak factors. Here we extract the first 6 factors with RP-PCA $( \gamma = 1 0 )$ and PCA. In addition, we include the popular Fama–French 5 factors (market, size, value, profitability and investment) from Kenneth French’s website. The variance signal is defined as the largest eigenvalues of $\varLambda \varSigma _ { F } \varLambda ^ { \intercal }$ . We normalize these eigenvalues by the same constant $\begin{array} { r } { \sigma _ { e } ^ { 2 } = \frac { 1 } { N } \sum _ { i = 1 } ^ { \tt N } { \sigma _ { e , i } ^ { 2 } } } \end{array}$ based on the residuals from 6 PCA factors.34 This makes the variance signals comparable to our simulation design. The 5th factor has a variance signal around 0.05 which based on our simulation is well described by a weak factor model. The simulations also predict that these weak factors can be better estimated by RP-PCA if they have a large Sharpe-ratio. This is exactly what we observe in the data. 


Table 2 Deciles of 37 single-sorted portfolios from 07/1963 to 12/2016 $( N = 3 7 0$ and $T = 6 5 0 ) \mathrm { ; }$ Variance signal for different factors: Largest eigenvalues of $\varLambda \varSigma _ { F } \varLambda ^ { \intercal }$ normalized by the average idiosyncratic variance $\begin{array} { r } { \sigma _ { e } ^ { 2 } = \frac { 1 } { N } \sum _ { i = 1 } ^ { N } \sigma _ { e , i } ^ { 2 } } \end{array}$ .


<table><tr><td></td><td>PCA</td><td>RP-PCA (<eq>\gamma = 10</eq>)</td><td>FF5</td></tr><tr><td><eq>\sigma_{1}^{2}</eq></td><td>8.05</td><td>8.05</td><td>8.00</td></tr><tr><td><eq>\sigma_{2}^{2}</eq></td><td>0.27</td><td>0.27</td><td>0.21</td></tr><tr><td><eq>\sigma_{3}^{2}</eq></td><td>0.21</td><td>0.21</td><td>0.17</td></tr><tr><td><eq>\sigma_{4}^{2}</eq></td><td>0.14</td><td>0.14</td><td>0.03</td></tr><tr><td><eq>\sigma_{5}^{2}</eq></td><td>0.05</td><td>0.05</td><td>0.02</td></tr><tr><td><eq>\sigma_{6}^{2}</eq></td><td>0.03</td><td>0.04</td><td>0.00</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/a875644aa1d48b7459e3585283d000173d12727136b548f2235009d541536fc3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/a212805ac78e4351671e2a3e71ffb9a633c5e50ed8442449ba17efbe1a98e61c.jpg)



Fig. 9. Deciles of 37 single-sorted portfolios from 07/1963 to 12/2016 $( N = 3 7 0$ and $T \ : = \ : 6 5 0 ) $ : Largest normalized eigenvalues of the matrix $\begin{array} { r } { \frac { 1 } { N } \left( \frac { 1 } { T } X ^ { \top } X + \gamma \bar { X } \bar { X } ^ { \top } \right) } \end{array}$ for different RP-weights γ . Left plot: Eigenvalues are normalized by division through the average idiosyncratic variance $\begin{array} { r } { \sigma _ { e } ^ { 2 } = \frac { 1 } { N } \sum _ { i = 1 } ^ { N } \sigma _ { e , i } ^ { 2 } } \end{array}$ estimated by the average of the non-systematic PCA eigenvalues. Right plot: Eigenvalues are normalized by the corresponding PCA $( \gamma = - 1 )$


The left plot in Fig. 9 shows the eigenvalues of the matrix ${ \textstyle \frac { 1 } { N } } \left( { \frac { 1 } { T } } X ^ { \top } X + \gamma { \bar { X } } { \bar { X } } ^ { \top } \right)$ normalized by the average idiosyncratic N Tvariance. Our weak factor model predicts that the signal of this matrix should be larger for RP-PCA compared to PCA. The eigenvalue curves confirm that the signal for the weaker factors clearly separates from the PCA signal. $\gamma = 1 0$ seems to be sufficient for strengthening the signal. The right plot in Fig. 9 normalizes the eigenvalues by the corresponding PCA eigenvalues. In particular the signal for the 5th factor is strengthened. 

# 8. Conclusion

We develop a new estimator for latent asset pricing factors from large data sets. Our estimator is essentially a regularized version of PCA that puts a penalty on the pricing error. We derive the asymptotic distribution theory under weak and strong factor model assumptions and show that our estimator RP-PCA strongly dominates conventional PCA. We can detect weak factors with high Sharpe-ratios which are undetectable with PCA. Strong factors are estimated more efficiently with RP-PCA compared to PCA. 

# Appendix A. Simulation

See Figs. A.10 and A.11. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/9121722283b1dae5e7e05945c00d1b69bf51057beca93ae664739e8e69031d41.jpg)



Fig. A.10. N = 370, T = 650: Correlations and Sharpe-ratios as a function of the RP-weight γ for different variances and Sharpe-ratios. The residuals have a cross-sectional correlation defined by the band-diagonal matrix.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/d92c4e1a8d3ecb80d90949582ca3d5c03238d79fecf22dcd3bdcd5315c24d929.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/a2c23c0c6c4891269059010ed5347fe55ab6b5c868290efe79d02e7cb01092e9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/21bfe192edb73d06e2cbb99852742f1149a3648ae8533112853a45ecc6f698ed.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/ef98e1daf45addc422baed26f475194f3dc3449cce11bbd2dacad5c323741a70.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/1ab802f101502ee26c2943a959add7960bd129c1bd123bd27464ba9fa1a480ab.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/136a432538aff5a0771804ce13819ebd9aef042c99e616d7f4ca916c0473bbc5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/6229750c0677d77e559ddb2213d2f08048aee13e96121fea674061fe02028fe8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/5008a8befcd371abb61cfd2c00decf40a2e58cbacb59c3cb9fe4d9477b5be671.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/e45349ce84bbe9b1b275fd153e22e33c013fd130bda9e49854971ee2111c3921.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/8ae687efe8fbba18b83909d15ca19fdade01a12fad57d155ffbf1b0114e30838.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/7bc559fc037f9d3be9f9cebcc82ac3e8f1eae4b0aec6cbaf4041eb2ae7fbec86.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/745121837b2b4a320e22bb39e215a157ca44fc001078cf60f17772d14d713eea.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/2d2ddaef23bd9a8f8a60b6fdd351a38378e98626fbe4044dbdd826379d1d0763.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/4179d137072b2556cfd2e4886c81b624d72ebfa5de6b481a3b46d8ee86694b7e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/6e06f7e915866129580a8624a3a0d77cae448c0eadb8af99bc2a0f88e99a7604.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-20/4b1033a6-a828-47ec-ab71-5531fb656364/2f57aaefe1a57af25a91debfadfbf9cb5daa97dd0f38fb146104a9f6abcdd4ea.jpg)



Fig. A.11. $N = 3 7 0 , T = 6 5 0 ;$ : Upper and lower bounds for the correlations and the parameter ρ as a function of the RP-weight $\gamma$ for different variances and Sharpe-ratios. The residuals have a cross-sectional correlation defined by the band-diagonal matrix.


# Appendix B. Proofs for the weak factor model

We only prove the statements for RP-PCA. The statements for the conventional PCA based on the covariance matrix are a special case. Given an $N \times N$ matrix A we denote the sorted eigenvalues by $\lambda _ { 1 } ( A ) \geq \cdots \geq \lambda _ { N } ( A )$ . Let $\phi _ { A } ( z )$ be the empirical eigenvalue distribution, i.e. the probability measure defined as $\begin{array} { r } { \phi _ { A } ( z ) = \frac { 1 } { N } \sum _ { i = 1 } ^ { N } \delta _ { \lambda _ { i } ( A ) } } \end{array}$ N  where $\delta _ { x }$ Ais the Dirac measure. In our case the probability measure $\phi _ { A }$ converges almost surely weakly for $T \to \infty$ (and therefore also $N \to \infty$ as $\begin{array} { r } { \frac { N } { T } \ \to \ c > \ 0 } \end{array}$ and N and T are asymptotically proportional). We first prove the results for $\varSigma = \sigma _ { e } ^ { 2 } I _ { N }$ . Then we show how to modify the proof for a general Σ. 

Proof of Theorem 2. Instead of using $\scriptstyle { \frac { 1 } { T } } X ^ { \top } W ^ { 2 } X$ we study $\scriptstyle { \frac { 1 } { T } } W X X ^ { \top } W$ with $\begin{array} { r } { W = I _ { T } + \frac { \tilde { \gamma } } { \tau } \mathbb { 1 } \mathbb { 1 } ^ { \top } } \end{array}$ and $\widetilde { \gamma } = \sqrt { \gamma + 1 } - 1$ . Define the orthonormal matrix $U = ( U _ { 1 } , U _ { 2 } )$ T consisting of the $T \times \dot { K } + 1$ matrix $U _ { 1 }$ and the $T \times T - K - 1$ matrix $U _ { 2 }$ by 

$$
U _ {1} = \left(\left(I _ {T} - \frac {1}{T} \mathbb {1} \mathbb {1} ^ {\top}\right) \frac {F}{\sqrt {T}} \quad \frac {\mathbb {1}}{\sqrt {T}}\right) \left( \begin{array}{c c} \left(\frac {1}{T} F ^ {\top} (I _ {T} - \frac {1}{T} \mathbb {1} \mathbb {1} ^ {\top}) F\right) ^ {- 1 / 2} & 0 \\ 0 & 1 \end{array} \right) \tilde {U},
$$

where the $K + 1 \times K + 1$ matrix $\tilde { U }$ consists of the orthonormal eigenvectors of the ‘‘signal matrix’’ $M _ { \mathrm { R P - P C A } }$ : 

$$
\tilde {U} ^ {\top} \left( \begin{array}{c c} \Sigma_ {F} + c \sigma_ {e} ^ {2} & \Sigma_ {F} ^ {1 / 2} \mu_ {F} (1 + \tilde {\gamma}) \\ \mu_ {F} ^ {\top} \Sigma_ {F} ^ {1 / 2} (1 + \tilde {\gamma}) & (1 + \gamma) (\mu_ {F} ^ {\top} \mu_ {F} + c \sigma_ {e} ^ {2}) \end{array} \right) \tilde {U} = \left( \begin{array}{c c c} \theta_ {1} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & \theta_ {K + 1} \end{array} \right).
$$

$U _ { 2 }$ are orthonormal vectors orthogonal to $U _ { 1 } ,$ , i.e. $U _ { 1 } ^ { \top } U _ { 2 } = 0$ and $U _ { 2 } ^ { \top } U _ { 2 } = I _ { T - K - 1 }$ 

We now analyze the spectrum of $\begin{array} { r } { S : = \frac { 1 } { T } U ^ { \top } W X \dot { X } ^ { \top } } \end{array}$ WU, which has the same non-zero eigenvalues as ${ \scriptstyle { \frac { 1 } { T } } } X ^ { \top } W ^ { 2 } X$ 

$$
S = \left( \begin{array}{c c} S _ {1 1} & S _ {1 2} \\ S _ {2 1} & S _ {2 2} \end{array} \right) = \left( \begin{array}{c c} \frac {1}{T} U _ {1} ^ {\top} W (F \varLambda^ {\top} + e) (F \varLambda^ {\top} + e) ^ {\top} W U _ {1} & \frac {1}{T} U _ {1} ^ {\top} W (F \varLambda^ {\top} + e) e ^ {\top} W U _ {2} \\ \frac {1}{T} U _ {2} ^ {\top} W e (\varLambda F ^ {\top} + e ^ {\top}) W U _ {1} & \frac {1}{T} U _ {2} ^ {\top} W e e ^ {\top} W U _ {2} \end{array} \right).
$$

An eigenvalue of S that is not an eigenvalue of $S _ { 2 2 }$ satisfies 

$$
0 = \det (\lambda I _ {T} - S) = \det (\lambda I _ {T - K - 1} - S _ {2 2}) \det (\lambda I _ {K + 1} - \kappa_ {T} (\lambda))
$$

with 

$$
\kappa_ {T} (\lambda) = S _ {1 1} + S _ {1 2} \left(\lambda I _ {T - K - 1} - S _ {2 2}\right) ^ {- 1} S _ {2 1}.
$$

For sufficiently large T it holds ${ \sf d e t } ( \lambda I _ { T - K - 1 } - S _ { 2 2 } ) \neq 0$ for the first $K + 1$ eigenvalues. Therefore, the first $K + 1$ eigenvalues satisfy 

$$
\det (\lambda I _ {K + 1} - \kappa_ {T} (\lambda)) = 0.
$$

We want to study the limiting behavior of $\kappa _ { T } ( \lambda )$ for $T \to \infty$ . 

$$
\begin{array}{l} \kappa_ {T} (\lambda) = \frac {1}{T} \left(U _ {1} ^ {\top} W (F \Lambda^ {\top} + e)\right) \left(I _ {N} + \frac {1}{T} e ^ {\top} W U _ {2} \left(\lambda I _ {T - K - 1} - \frac {1}{T} U _ {2} ^ {\top} W e e ^ {\top} W U _ {2}\right) ^ {- 1} U _ {2} ^ {\top} W e\right) \\ \cdot \left(U _ {1} ^ {\top} W (F \Lambda^ {\top} + e)\right) ^ {\top} \\ = \frac {\lambda}{T} \left(U _ {1} ^ {\top} W (F \Lambda^ {\top} + e)\right) \left(\lambda I _ {N} - \frac {1}{T} e ^ {\top} W U _ {2} U _ {2} ^ {\top} W e\right) ^ {- 1} \left(U _ {1} ^ {\top} W (F \Lambda^ {\top} + e)\right) ^ {\top}, \\ \end{array}
$$

where we have used the identify that for $\lambda \neq 0$ which is not an eigenvalue of $A ^ { \top } A$ it holds $I _ { N } + A ( \lambda I _ { T } - A ^ { \top } A ) ^ { - 1 } A ^ { \top } =$ $\lambda ( \lambda I _ { N } - A A ^ { \top } ) ^ { - 1 }$ . 

By Lemma A.2 in Benaych-Georges and Nadakuditi (2011) it holds first 

$$
\frac {\lambda}{T} \left(U _ {1} ^ {\top} W (F \Lambda^ {\top})\right) \left(\lambda I _ {N} - \frac {1}{T} e ^ {\top} W U _ {2} U _ {2} ^ {\top} W e\right) ^ {- 1} \left(U _ {1} ^ {\top} W (F \Lambda^ {\top})\right) ^ {\top}
$$

$$
= \lambda \left(\frac {1}{T} U _ {1} ^ {\top} W F F ^ {\top} W U _ {1}\right) \frac {1}{N} \operatorname{trace} \left(\left(\lambda I _ {N} - \frac {1}{T} e ^ {\top} W U _ {2} U _ {2} ^ {\top} W e\right) ^ {- 1}\right) + o _ {p} (1),
$$

and second by the law of large numbers 

$$
\frac {\lambda}{T} \left(U _ {1} ^ {\top} W e\right) \left(\lambda I _ {N} - \frac {1}{T} e ^ {\top} W U _ {2} U _ {2} ^ {\top} W e\right) ^ {- 1} \left(U _ {1} ^ {\top} W e\right) ^ {\top} \tag {B.1}
$$

$$
= \lambda \left(U _ {1} ^ {\top} W U _ {1}\right) \cdot \sigma_ {e} ^ {2} \frac {N}{T} \frac {1}{N} \operatorname{trace} \left(\left(\lambda I _ {N} - \frac {1}{T} e ^ {\top} W U _ {2} U _ {2} ^ {\top} W e\right) ^ {- 1}\right) + o _ {p} (1). \tag {B.2}
$$

Here, we made use of the following argument. Because of the orthonormality we have $U _ { 2 } ^ { \top } e \operatorname { = : } \tilde { e }$ with $\tilde { e } _ { t } \stackrel { i . i . d . } { \sim } N ( 0 , \Sigma )$ . Note that $U _ { 2 } ^ { \top } W = U _ { 2 } ^ { \top }$ by construction. For any matrix C independent of $U _ { 1 } ^ { \top }$ We the following expected value conditional on C equals 

$$
E \left[ U _ {1} ^ {\top} W e C e ^ {\top} W U _ {1} | C \right] = \operatorname{trace} (\Sigma C) \cdot U _ {1} ^ {\top} W U _ {1} = \operatorname{trace} (\Sigma C) \cdot \tilde {U} ^ {\top} \left( \begin{array}{c c} I _ {K} & 0 \\ 0 & 1 + \gamma \end{array} \right) \tilde {U}.
$$

For $\Sigma = \sigma _ { e } ^ { 2 } I _ { N }$ it holds that trace $\mathbf { \nabla } ^ { \prime } \Sigma ( ) = \sigma _ { e } ^ { 2 } \mathbf { t r a c e } ( C )$ , which is crucial for the result. This is the main term that we need to treat differently for the case of a general residual covariance matrix. 

Last but not least we have 

$$
\frac {\lambda}{T} \left(U _ {1} ^ {\top} W (F \varLambda^ {\top})\right) \left(\lambda I _ {N} - \frac {1}{T} e ^ {\top} W U _ {2} U _ {2} ^ {\top} W e\right) ^ {- 1} \left(U _ {1} ^ {\top} W e\right) ^ {\top} = o _ {p} (1).
$$

Note that $\textstyle \frac { 1 } { \sqrt { N } } \epsilon ^ { \top }$ has orthogonally invariant column vectors by the properties of the normal distribution and it holds that $e ^ { \top } W U _ { 2 } U _ { 2 } ^ { \top }$ ⊤We is independent from $U _ { 1 }$ despite the dependence of $U _ { 1 }$ and $U _ { 2 }$ . Hence Lemma A.2 in Benaych-Georges and Nadakuditi (2011) applies. In summary, $\kappa _ { T }$ is described by 

$$
\begin{array}{l} \kappa_ {T} (\lambda) = \lambda \tilde {U} ^ {\top} \left(\left( \begin{array}{c c} \Sigma_ {F} & \Sigma_ {F} ^ {1 / 2} \mu_ {F} (1 + \tilde {\gamma}) \\ \mu_ {F} ^ {\top} \Sigma_ {F} ^ {1 / 2} (1 + \tilde {\gamma}) & \mu_ {F} ^ {\top} \mu_ {F} (1 + \gamma) \end{array} \right) + c \cdot \sigma_ {e} ^ {2} \left( \begin{array}{c c} I _ {K} & 0 \\ 0 & 1 + \gamma \end{array} \right)\right) \tilde {U} \\ \cdot \frac {1}{N} \operatorname{trace} \left(\left(\lambda I _ {N} - \frac {1}{T} e ^ {\top} W U _ {2} U _ {2} ^ {\top} W e\right) ^ {- 1}\right) + o _ {p} (1). \\ \end{array}
$$

As $U _ { 2 } ^ { \top } W e = U _ { 2 } ^ { \top } e = \tilde { e }$ with $\tilde { e } _ { t } \stackrel { i . i . d . } { \sim } N ( 0 , \Sigma )$ for $t = 1 , \ldots , T - K - 1$ we have 

$$
\kappa_ {T} (\lambda) \xrightarrow {p} \kappa (\lambda) = \lambda \tilde {U} ^ {\top} M _ {\mathrm{RP-PCA}} \tilde {U} G (\lambda).
$$

Therefore, λ is an eigenvalue of the matrix $\lambda \left( \begin{array} { c c c } { { \theta _ { 1 } } } & { { \cdots } } & { { 0 } } \\ { { \vdots } } & { { \ddots } } & { { \vdots } } \\ { { 0 } } & { { \cdots \cdot } } & { { \theta _ { K + 1 } ^ { \prime } } } \end{array} \right) G ( \lambda )$ respectively 1 is an eigenvalue of the matrix $\left( \begin{array} { c c c } { \theta _ { 1 } } & { \cdots } & { 0 } \\ { \vdots } & { \ddots } & { \vdots } \\ { 0 } & { \cdots } & { \theta _ { K + 1 } } \end{array} \right)$ G(λ) which is equivalent to 

$$
G (\lambda) = \frac {1}{\theta_ {i}} \quad \text { respectively } \quad \lambda = G ^ {- 1} \left(\frac {1}{\theta_ {i}}\right) \quad \text { for   some } i = 1, \dots , K + 1.
$$

If a solution outside the support of the spectrum of $S _ { 2 2 }$ exists, then it must satisfy the equation $\begin{array} { r } { G ( \lambda ) \ = \ \frac { 1 } { \theta _ { i } } } \end{array}$ for some $i = 1 , \ldots , K + 1$ θi. Otherwise by Weyl’s inequality and the same arguments as in Benaych-Georges and Nadakuditi (2011) $\lambda { \overset { p } { \to } } b .$ . For $z > b$ we have $G ^ { \prime } ( z ) < 0$ . Therefore, if $\begin{array} { r } { \theta _ { i } > \frac { 1 } { G ( b ) } } \end{array}$ then a solution exists. If $\begin{array} { r } { \theta _ { i } < \frac { 1 } { G ( b ) } } \end{array}$ then no solution exists and $\lambda { \overset { p } { \to } } b .$ 

Recall that the estimators for the loadings and factors are defined as follows: $\hat { \boldsymbol A }$ are the first K eigenvectors of ${ \scriptstyle { \frac { 1 } { T } } } X ^ { \top } W ^ { 2 } X$ and $\hat { \boldsymbol F } = \boldsymbol X \hat { \boldsymbol A }$ . For the proofs we will use an equivalent formulation. Denote by $P$ the first K eigenvectors of $\begin{array} { r } { \frac { 1 } { T } U ^ { \top } W X X ^ { \top } W U } \end{array}$ . Then $\hat { \boldsymbol { \Lambda } } = \boldsymbol { X } ^ { \top } \boldsymbol { W } \boldsymbol { U } \boldsymbol { P } \hat { \boldsymbol { D } } _ { K } ^ { - 1 / 2 }$ , where $\hat { D } _ { K }$ is a diagonal matrix with the first K largest eigenvalues of ${ \scriptstyle \frac { 1 } { T } } U ^ { \top } X ^ { \top } W ^ { 2 } X U$ , i.e. 

$$
\frac {1}{T} P ^ {\top} U ^ {\top} W X X ^ {\top} W U P = \hat {D} _ {K}.
$$

The estimator of the factors takes the form $\hat { F } = X \hat { \lambda } = \sqrt { T } W ^ { - 1 } U P D _ { \scriptscriptstyle K } ^ { \scriptscriptstyle { 1 / 2 } }$ 

We analyze the $K + 1$ eigenvectors of $\begin{array} { r } { \frac 1 T U ^ { \top } W X X ^ { \top } W U . \ A s s u m e \ p _ { i } } \end{array}$ is an eigenvector of S associated with $\lambda _ { i } { \mathrm { : } }$ 

$$
\left( \begin{array}{c c} \lambda_ {i} I _ {K + 1} - S _ {1 1} & - S _ {1 2} \\ - S _ {2 1} & \lambda_ {i} I _ {T - K - 1} - S _ {2 2} \end{array} \right) \binom{p _ {i, 1}}{p _ {i, 2}} = \binom{0}{0},
$$

where $p _ { i , 1 }$ and $p _ { i , 2 }$ are the first $K + 1$ respectively last $T - K - 1$ components of the vector $p _ { i } .$ . Hence 

$$
p _ {2, i} = (\lambda_ {i} I _ {T - K - 1} - S _ {2 2}) ^ {- 1} S _ {2 1} p _ {i, 1}
$$

$$
0 = (\lambda_ {i} I _ {K + 1} - \kappa_ {T} (\lambda_ {i})) p _ {i, 1}.
$$

Assume that $\theta _ { i } > \theta _ { c r i t }$ , i.e. $\operatorname* { d e t } ( \lambda _ { i } I _ { K + 1 } - \kappa _ { T } ( \lambda _ { i } ) ) = o _ { p } ( 1 )$ . Consequently 

$$
\left(I _ {K + 1} - \theta_ {i} ^ {- 1} \left( \begin{array}{c c c} \theta_ {1} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & \theta_ {K + 1} \end{array} \right)\right) p _ {i, 1} = o _ {p} (1).
$$

Thus, the vector $p _ { i , 1 }$ has all elements converging to zero in probability except at the ith position: 

$$
p _ {i, 1} ^ {\top} = \left( \begin{array}{c c c c c c} 0 & \dots 0 & \| p _ {i, 1} \| & 0 & \dots & 0 \end{array} \right) + o _ {p} (1).
$$

where $\| p _ { i , 1 } \|$ denotes the length of the vector which is completely determined by the ith element. The vector $p _ { i , 2 }$ satisfies 

$$
\begin{array}{l} p _ {i, 2} ^ {\top} p _ {i, 2} = p _ {i, 1} ^ {\top} S _ {1 2} \left(\lambda_ {i} I _ {T - K - 1} - S _ {2 2}\right) ^ {- 2} S _ {2 1} p _ {i, 1} \\ = p _ {i, 1} ^ {\top} \frac {1}{T} U _ {1} ^ {\top} W \left(F \Lambda^ {T} + e\right) \left(e ^ {\top} W U _ {2} \left(\lambda_ {i} I _ {T - K - 1} - S _ {2 2}\right) ^ {- 2} U _ {2} ^ {\top} W e\right) \left(F \Lambda^ {T} + e\right) ^ {\top} W U _ {1} p _ {i, 1}. \\ \end{array}
$$

By similar arguments as in the first part of the proof showing the convergence of $\kappa _ { T } ( \lambda )$ , it follows that 

$$
\begin{array}{l} p _ {i, 2} ^ {\top} p _ {i, 2} = p _ {i, 1} ^ {\top} \left( \begin{array}{c c c} \theta_ {1} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & \theta_ {K + 1} \end{array} \right) p _ {i, 1} \\ \cdot \frac {1}{N} \operatorname{trace} \left(e ^ {\top} W U _ {2} \left(\lambda_ {i} I _ {T - K - 1} - \frac {1}{T} U _ {2} ^ {\top} \operatorname{Wee} ^ {\top} W U _ {2}\right) ^ {- 2} U _ {2} ^ {\top} \operatorname{We}\right) + o _ {p} (1). \\ \end{array}
$$

Recall that $U _ { \gamma } ^ { \top } W e = \tilde { e }$ can be interpreted as $T - K - 1$ independent draws of a $N ( 0 , \Sigma )$ . Denote the eigenvalue distribution function of $\bar { \frac { 1 } { T } } \bar { \tilde { e } } ^ { \top } \tilde { e }$ by $\phi _ { T } ( z )$ and of $\scriptstyle { \frac { 1 } { T } } \tilde { e } \tilde { e } ^ { \top }$ by $\tilde { \phi } _ { T } ( z )$ . By assumption, both converge to limit spectral distribution functions that are related through $\tilde { \phi } ( z ) - c \phi ( z ) = ( 1 - c ) \delta _ { 0 }$ , where $\delta _ { 0 }$ is the Dirac-measure with point-mass at zero.35 By the properties of the trace operator 

$$
\frac {1}{N} \operatorname{trace} \left(e ^ {\top} W U _ {2} \left(\lambda_ {i} I _ {T - K - 1} - \frac {1}{T} U _ {2} ^ {\top} W e e ^ {\top} W U _ {2}\right) ^ {- 2} U _ {2} ^ {\top} W e\right) = \int \frac {z}{(\lambda_ {i} - z) ^ {2}} d \tilde {\phi} _ {T} (z),
$$

which converges almost surely to 

$$
\begin{array}{l} \int \frac {z}{(\lambda_ {i} - z) ^ {2}} d \tilde {\phi} (z) = \int \frac {z}{(\lambda_ {i} - z) ^ {2}} d (c \phi (z) + (1 - c) \delta_ {0}) \\ = c \int {\frac {z}{(\lambda_ {i} - z) ^ {2}}} d \phi (z) = B (\lambda_ {i}). \\ \end{array}
$$

Consequently 

$$
1 = \| p _ {i, 1} \| ^ {2} + \| p _ {i, 2} \| ^ {2} = p _ {i, 1} ^ {\top} p _ {i, 1} \left(1 + \theta_ {i} B (\lambda_ {i})\right) + o _ {p} (1)
$$

and therefore 

$$
\left\| p _ {i, 1} \right\| ^ {2} \xrightarrow {p} \frac {1}{1 + \theta_ {i} B (\lambda_ {i})}.
$$

Assume that $\theta _ { i } < \theta _ { c r i t }$ , i.e. ${ \operatorname* { d e t } } ( \lambda _ { i } I _ { K + 1 } - \kappa _ { T } ( \lambda _ { i } ) )$ does not converge to 0 asymptotically. It still holds 

$$
p _ {i, 2} ^ {\top} p _ {i, 2} = u _ {i, 1} ^ {\top} \left( \begin{array}{c c c} \theta_ {1} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & \theta_ {K + 1} \end{array} \right) u _ {i, 1} \lim _ {z \downarrow b} B (z)
$$

as $\lambda _ { i }$ converges in probability to b. If $\begin{array} { r } { \operatorname* { l i m } _ { z \downarrow b } B ( z ) = \infty } \end{array}$ , then $\| p _ { i , 1 } \| \overset { p } {  }$ 0 and 

$$
p _ {i, 1} ^ {\top} = \left( \begin{array}{c c c} 0 & \dots & 0 \end{array} \right) + o _ {p} (1).
$$

All we need to show is that $\theta _ { i } < \theta _ { c r i t }$ implies $\begin{array} { r } { \operatorname* { l i m } _ { z \downarrow b } B ( z ) = \infty } \end{array}$ . This follows for the largest eigenvalue $\lambda _ { 1 }$ by the same argument as in the proof of theorem 2.3 in Benaych-Georges and Nadakuditi (2011). If $K \ > \ 1$ we need in addition eigenvalue repulsion to show the result for $\lambda _ { i }$ for $i = 2 , \dots , K$ (see Nadakuditi (2014), appendix 7). Assume that the distance between the largest eigenvalues of the matrix $\scriptstyle { \frac { 1 } { T } } e ^ { \top } e$ decays with a certain rate 

$$
\left| \lambda_ {i + 1} \left(\frac {e ^ {\top} e}{T}\right) - \lambda_ {i} \left(\frac {e ^ {\top} e}{T}\right) \right| \leq O _ {p} \left(\frac {\log (N)}{N ^ {2 / 3}}\right).
$$

This is satisfied for normally distributed residuals as in our case (see Onatski (2012)). Hence, 

$$
\begin{array}{l} B (\lambda_ {i}) = c \int \frac {z}{(\lambda_ {i} - z) ^ {2}} d \tilde {\phi} _ {T} (z) + o _ {p} (1) \\ \geq O _ {p} \left(\frac {1}{N}\right) \cdot \frac {1}{\left(\lambda_ {1} \left(S _ {2 2}\right) - \lambda_ {K + 1} \left(S _ {2 2}\right)\right) ^ {2}} + o _ {p} (1) \\ \geq O _ {p} \left(\frac {N ^ {1 / 3}}{\log (N) ^ {2}}\right). \\ \end{array}
$$

which satisfies the explosion condition. 

We can now go back to the original problem: Define 

$$
\rho_ {i} = \left\{ \begin{array}{l l} \frac {1}{\sqrt {1 + \theta_ {i} B (G ^ {- 1} (\theta_ {i} ^ {- 1}))}} & \text { if } \theta_ {i} > \theta_ {c r i t} \\ 0 & \text { otherwise. } \end{array} \right.
$$

The estimator for the factors can now be written as 

$$
\hat {F} = \sqrt {T} W ^ {- 1} U P \hat {D} _ {K} ^ {1 / 2},
$$

where $P = { \binom { P _ { 1 } } { P _ { 2 } } }$ with the $( K + 1 ) \times K$ matrix $P _ { 1 } = \left( p _ { 1 , 1 } \cdot \cdot \cdot p _ { K , 1 } \right)$ and $P _ { 2 } = \left( p _ { 1 , 2 } \cdot \cdot \cdot p _ { K , 2 } \right)$ and 

$$
P _ {1} \stackrel {{p}} {{\to}} \left( \begin{array}{c c c c} \rho_ {1} & 0 & \dots & 0 \\ 0 & \rho_ {2} & \dots & 0 \\ 0 & 0 & \ddots & \vdots \\ 0 & \dots & 0 & \rho_ {K} \\ 0 & \dots & & 0 \end{array} \right) \qquad \hat {D} _ {K} = \left( \begin{array}{c c c} \hat {\theta} _ {1} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & \hat {\theta} _ {K} \end{array} \right) \qquad \qquad \hat {\theta} _ {i} \stackrel {{p}} {{\to}} \left\{ \begin{array}{l l} G ^ {- 1} \left(\frac {1}{\theta_ {i}}\right) & \text {if} \theta_ {i} > \theta_ {c r i t} \\ b & \text {otherwise.} \end{array} \right.
$$

We divide the calculation of $\widehat { \mathrm { C o r r } } ( F , \hat { F } )$ into two steps. First, we analyze the first two terms of the expression. Recall, that we denote by $\begin{array} { r } { M _ { 1 } = I _ { T } - \frac { 1 } { T } \mathbb { 1 } \mathbb { 1 } ^ { \top } } \end{array}$ the projection matrix that demeans the data and 0 denotes a matrix of zeros of appropriate dimension. 

$$
\begin{array}{l} \left(\frac {1}{T} F ^ {\top} M _ {1} F\right) ^ {- 1 / 2} \left(\frac {1}{T} F ^ {\top} M _ {1} \hat {F}\right) \\ = \left(\frac {1}{T} F ^ {\top} M _ {1} F\right) ^ {- 1 / 2} \left(\frac {\sqrt {T}}{T} F ^ {\top} M _ {1} W ^ {- 1} U P \hat {D} _ {K} ^ {1 / 2}\right) \\ = \left(\frac {1}{T} F ^ {\top} M _ {1} F\right) ^ {- 1 / 2} \left(\frac {1}{\sqrt {T}} F ^ {\top} M _ {1} \left( \begin{array}{c c} U _ {1} & U _ {2} \end{array} \right) P \hat {D} _ {K} ^ {1 / 2}\right) \\ = \left(\frac {1}{T} F ^ {\top} M _ {1} F\right) ^ {- 1 / 2} \left(\left(\left(\frac {1}{T} F ^ {\top} M _ {1} F \left(\frac {1}{T} F ^ {\top} M _ {1} F\right) ^ {- 1 / 2} \quad 0 _ {K \times 1}\right) \tilde {U} \quad \frac {1}{\sqrt {T}} F ^ {\top} M _ {1} U _ {2}\right) P \hat {D} _ {K} ^ {1 / 2}\right) \\ = \left(\left( \begin{array}{c c} I _ {K} & 0 _ {K \times 1} \end{array} \right) \tilde {U} \quad 0 _ {K \times T - K - 1}\right) P \hat {D} _ {K} ^ {1 / 2} \\ = \left( \begin{array}{c c} I _ {K} & 0 _ {K \times 1} \end{array} \right) \tilde {U} P _ {1} \hat {D} _ {K} ^ {1 / 2}. \\ \end{array}
$$

Here we have made used of the following results: As W $\begin{array} { r } { \mathrm { \Omega } ^ { - 1 } = I _ { T } - \frac { \tilde { \gamma } } { 1 + \tilde { \gamma } } \mathbb { 1 } \mathbb { 1 } ^ { \top } } \end{array}$ and $( 1 + \tilde { \gamma } ) ^ { 2 } = 1 + \gamma$ it follows that W ${ } ^ { \cdot 1 } M _ { 1 } = M _ { 1 }$ By orthogonality of $U _ { 1 }$ and $U _ { 2 }$ it holds that $F ^ { \top } M _ { 1 } U _ { 2 } = 0$ . Now we turn to the second term in $\widehat { \mathrm { C o r r } } ( F , \hat { F } )$ : 

$$
\begin{array}{l} \frac {1}{T} \hat {F} M _ {1} \hat {F} = \hat {D} _ {K} ^ {1 / 2} P ^ {\top} U ^ {\top} W ^ {- 1} M _ {1} W ^ {- 1} U P \hat {D} _ {K} ^ {1 / 2} \\ = \hat {D} _ {K} ^ {1 / 2} P ^ {\top} U ^ {\top} M _ {1} U P \hat {D} _ {K} ^ {1 / 2} \\ = \hat {D} _ {K} ^ {1 / 2} P ^ {\top} \left( \begin{array}{c c} U _ {1} ^ {\top} M _ {1} U _ {2} & U _ {1} ^ {\top} M _ {1} U _ {2} \\ U _ {2} M _ {1} U _ {1} & U _ {2} ^ {\top} M _ {1} U _ {2} \end{array} \right) P \hat {D} _ {K} ^ {1 / 2} \\ = \hat {D} _ {K} ^ {1 / 2} P ^ {\top} \left( \begin{array}{c c} U _ {1} ^ {\top} M _ {1} U _ {2} & 0 _ {K + 1 \times T - K - 1} \\ 0 _ {T - K - 1 \times K + 1} & U _ {2} ^ {\top} U _ {2} \end{array} \right) P \hat {D} _ {K} ^ {1 / 2} \\ = \hat {D} _ {K} ^ {1 / 2} \left(P _ {1} ^ {\top} \tilde {U} ^ {\top} \left( \begin{array}{c c} I _ {K} & 0 _ {K \times 1} \\ 0 _ {1 \times K} & 0 \end{array} \right) \tilde {U} P _ {1} + P _ {2} ^ {\top} P _ {2}\right) \hat {D} _ {K} ^ {1 / 2}. \\ \end{array}
$$

Because of the orthogonality of $U _ { 1 }$ and $U _ { 2 }$ and the special structure of $U _ { 1 }$ we have $U _ { 1 } ^ { \top } M _ { 1 } U _ { 2 } = 0$ . Furthermore, it holds $U _ { 2 } ^ { \top } M _ { 1 } U _ { 2 } = I _ { T - K - 1 }$ . Finally, by the properties of $p _ { i , 2 }$ proven before we have 

$$
P _ {2} ^ {\top} P _ {2} \xrightarrow {p} \left( \begin{array}{c c c} 1 - \rho_ {1} ^ {2} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & 1 - \rho_ {K} ^ {2} \end{array} \right).
$$

This proves the limit expression for $\widehat { \mathrm { C o r r } } ( F , \hat { F } )$ . Note, that the sample mean of $\hat { F }$ satisfies 

$$
\hat {\mu} _ {\hat {F}} = \frac {1}{1 + \tilde {\gamma}} \left(0 _ {K \times K} \right. \left. \mathbb {1} _ {K}\right) \tilde {U} P _ {1} \hat {D} _ {K} ^ {1 / 2}.
$$

If $\gamma > - 1$ and $\mu _ { F } \neq 0 ,$ , then the first K eigenvalues of $M _ { \mathrm { R P - P C A } }$ are strictly larger than the first K eigenvalues of $M _ { \mathrm { P C A } } ,$ i.e. 

$$
\theta_ {i} ^ {\mathrm{RP-PCA}} > \theta_ {i} ^ {\mathrm{PCA}}.
$$

This is a direct consequence of result (12) on page 75 in Lütkepohl (1996). 

# Proof for Cauchy transform with i.i.d. residuals.

For the special case where $e _ { t , i }$ i.i.d. $N ( 0 , \sigma _ { e } ^ { 2 } )$ , i.e. $\Sigma = \sigma _ { e } ^ { 2 } I _ { N }$ , the matrix $\scriptstyle { \frac { 1 } { T } } e ^ { \top } e$ follows the Marcenko–Pastur law: ˘ 

$$
d \phi (z) = \frac {1}{2 \pi c \sigma_ {e} ^ {2} z} \sqrt {(b - z) (z - a)} \mathbb {1} _ {\{z \in (a, b) \}} d z + \max \left(0, 1 - \frac {1}{c}\right) \delta_ {0}
$$

with 

$$
a = \sigma_ {e} ^ {2} (1 - \sqrt {c}) ^ {2}
$$

$$
b = \sigma_ {e} ^ {2} (1 + \sqrt {c}) ^ {2}
$$

a and b are the smallest respectively largest eigenvalue. For simplicity take $c > 1$ , but the results can be easily extended to the case $0 < c < 1$ . The object of interest is the Cauchy transform of the eigenvalue distribution function. Calculations as outlined in Bai and Silverstein (2010) lead to 

$$
G (z) = \frac {z - \sigma_ {e} ^ {2} (1 - c) - \sqrt {(z - \sigma_ {e} ^ {2} (1 + c)) ^ {2} - 4 c \sigma_ {e} ^ {2}}}{2 c z \sigma_ {e} ^ {2}}.
$$

Simple but tedious calculations show that 

$$
G ^ {- 1} (z) = \frac {z \sigma_ {e} ^ {2} (1 - c) + 1}{z - c \sigma_ {e} ^ {2} z ^ {2}}.
$$

Proof of Theorem 3. The proof for a general residual covariance matrix Σ is identical to the special case of $\varSigma = \sigma _ { e } ^ { 2 } I _ { N }$ up to Eq. (B.1). We want to study the limiting behavior of $\kappa _ { T } ( \lambda )$ for $T \to \infty$ . 

$$
\kappa_ {T} (\lambda) = \frac {\lambda}{T} \left(U _ {1} ^ {\top} W (F \Lambda^ {\top} + e)\right) \left(\lambda I _ {N} - \frac {1}{T} e ^ {\top} W U _ {2} U _ {2} ^ {\top} W e\right) ^ {- 1} \left(U _ {1} ^ {\top} W (F \Lambda^ {\top} + e)\right) ^ {\top}.
$$

By the law of large numbers we have 

$$
\begin{array}{l} \frac {\lambda}{T} \left(U _ {1} ^ {\top} W e\right) \left(\lambda I _ {N} - \frac {1}{T} e ^ {\top} W U _ {2} U _ {2} ^ {\top} W e\right) ^ {- 1} \left(U _ {1} ^ {\top} W e\right) ^ {\top} \\ = \lambda \left(U _ {1} ^ {\top} W U _ {1}\right) \cdot \frac {N}{T} \frac {1}{N} \operatorname{trace} \left(\Sigma \left(\lambda I _ {N} - \frac {1}{T} e ^ {\top} W U _ {2} U _ {2} ^ {\top} W e\right) ^ {- 1}\right) + o _ {p} (1), \\ \end{array}
$$

which is different from the expression in the special case of $\varSigma = \sigma _ { e } ^ { 2 } I _ { N }$ . Hence, the limiting expression of $\kappa _ { T }$ takes a more complicated form: 

$$
\begin{array}{l} \kappa_ {T} (\lambda) = \lambda \tilde {U} ^ {\top} \Bigg (\left( \begin{array}{c c} \Sigma_ {F} & \Sigma_ {F} ^ {1 / 2} \mu_ {F} (1 + \tilde {\gamma}) \\ \mu_ {F} ^ {\top} \Sigma_ {F} ^ {1 / 2} (1 + \tilde {\gamma}) & \mu_ {F} ^ {\top} \mu_ {F} (1 + \gamma) \end{array} \right) G (\lambda) \\ +   c \left( \begin{array}{c c} I _ {K} & 0 \\ 0 & 1 + \gamma \end{array} \right). \frac {1}{N}   \text {trace} \left(\varSigma \left(\lambda I _ {N} - \frac {1}{T} e ^ {\top} W e\right) ^ {- 1}\right) \Bigg) \tilde {U} + o _ {p} (1). \\ \end{array}
$$

Therefore, we obtain asymptotic lower and upper bounds (in a positive definite sense): 

$$
\lambda \tilde {U} ^ {\top} \underline {{M}} _ {R P - P C A, G} \tilde {U} G (\lambda) + o _ {p} (1) \leq \kappa_ {T} (\lambda) \leq \lambda \tilde {U} ^ {\top} \bar {M} _ {R P - P C A, G} \tilde {U} G (\lambda) + o _ {p} (1).
$$

The arguments of the derivation still hold when we replace $\tilde { U }$ by $U _ { G }$ or $\bar { U } _ { G } ,$ , i.e. we use a different rotation for defining $U _ { 1 }$ at the beginning of the proof, which then also results in a different rotation of $\kappa _ { T } ( \lambda )$ in order to obtain a diagonal matrix for the bounds. Denote by $\kappa _ { T , \underline { { U } } _ { G } } ( \lambda )$ and $\kappa _ { T , \bar { U } _ { G } } ( \lambda )$ the corresponding replacements of U˜ . We have 

$$
\left( \begin{array}{c c c} \underline {{\theta}} _ {1, G} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & \underline {{\theta}} _ {K + 1, G} \end{array} \right) G (\lambda) + o _ {p} (1) \leq \frac {\kappa_ {T , \underline {{U}} _ {G}} (\lambda)}{\lambda}
$$

$$
\left( \begin{array}{c c c} \bar {\theta} _ {1, G} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & \bar {\theta} _ {K + 1, G} \end{array} \right) G (\lambda) + o _ {p} (1) \geq \frac {\kappa_ {T , \bar {U} _ {G}} (\lambda)}{\lambda},
$$

which implifunction of $G ( \lambda ) \underline { { \theta } } _ { i , G } ~ \le ~ 1$ and e the $G ( \lambda ) \bar { \theta } _ { i , G } \geq 1$ . Note that ive is alwa $\begin{array} { r } { G ( \lambda ) = \int \frac { 1 } { \lambda - z } d \phi ( z ) } \end{array}$ $\phi ( z )$ nval for ibution. Thus, $\scriptstyle { \frac { 1 } { T } } e ^ { \top } e$ $\begin{array} { r } { \frac { \partial G ( \lambda ) } { \partial \lambda } ~ = ~ - \int \frac { 1 } { ( \lambda - z ) ^ { 2 } } d \phi ( z ) ~ < ~ 0 } \end{array}$ ∫ 1(λ−z)2 dφ(z) < 0 λ > b $\lambda ~ > ~ b$ ∂λ $\lambda \geq G ^ { - 1 } \left( \frac { \mathbf { \sigma } _ { 1 } } { \underline { { \theta } } _ { i , G } } \right)$ θ i,G and $\begin{array} { r } { \lambda \le G ^ { - 1 } \left( \frac { 1 } { \bar { \theta } _ { i , G } } \right) } \end{array}$ θ¯ if $\underline { { \theta } } _ { i , G } , \bar { \theta } _ { i , G } \geq \theta _ { c r i t }$ . Otherwise the bounds converge to b. 

The proof for the correlation follows similar arguments as in the special case of $\varSigma = \sigma _ { e } ^ { 2 } I _ { N }$ . We replace the rotation $\tilde { U }$ in the definition of $U _ { 1 }$ by $\underline { { U } } _ { B }$ and $\bar { U } _ { B }$ and obtain $\kappa _ { T , \underline { { U } } _ { B } } ( \lambda )$ respectively $\kappa _ { T , \bar { U } _ { B } } ( \lambda )$ . Here we present the proof for the lower bound but the arguments for the upper bound are analogously. We analyze the $K + 1$ eigenvectors of $\scriptstyle { \frac { 1 } { T } } U ^ { \top } W X X ^ { \top } W U$ . Assume $p _ { i }$ is an eigenvector of S associated with $\lambda _ { i } { \mathrm { : } }$ 

$$
\left( \begin{array}{c c} \lambda_ {i} I _ {K + 1} - S _ {1 1} & - S _ {1 2} \\ - S _ {2 1} & \lambda_ {i} I _ {T - K - 1} - S _ {2 2} \end{array} \right) \binom{p _ {i, 1}}{p _ {i, 2}} = \binom{0}{0},
$$

where $p _ { i , 1 }$ and $p _ { i , 2 }$ are the first $K + 1$ respectively last $T - K - 1$ components of the vector $p _ { i } .$ . Hence 

$$
p _ {2, i} = (\lambda_ {i} I _ {T - K - 1} - S _ {2 2}) ^ {- 1} S _ {2 1} p _ {i, 1}
$$

$$
0 = \left(\lambda_ {i} I _ {K + 1} - \kappa_ {T, \bar {U} _ {B}} (\lambda_ {i})\right) p _ {i, 1}.
$$

Assume that $\underline { { \theta } } _ { i , G } > \theta _ { c r i t }$ , i.e. $\lambda _ { i } I _ { K + 1 } - \kappa _ { T , \bar { U } _ { B } } ( \lambda _ { i } )$ has the eigenvalue 0. Consequently 

$$
\left(I _ {K + 1} - \frac {\kappa_ {T , \bar {U} _ {B}} (\lambda_ {i})}{\lambda_ {i}}\right) p _ {i, 1} = 0.
$$

$$
\left(I _ {K + 1} - \bar {U} _ {B} ^ {\top} \left(\left( \begin{array}{c c} \Sigma_ {F} & \Sigma_ {F} ^ {1 / 2} \mu_ {F} (1 + \tilde {\gamma}) \\ \mu_ {F} ^ {\top} \Sigma_ {F} ^ {1 / 2} (1 + \tilde {\gamma}) & (1 + \gamma) (\mu_ {F} ^ {\top} \mu_ {F}) \end{array} \right) G (\lambda_ {i}) + \left( \begin{array}{c c} I _ {K} & 0 \\ 0 & (1 + \gamma) \end{array} \right) c \cdot \tilde {G} (\lambda_ {i})\right) \bar {U} _ {B}\right) p _ {i, 1} = o _ {p} (1)
$$

and we define $V _ { i } : = { \bar { U } } _ { B } p _ { i , 1 } / \| p _ { i , 1 } \|$ as the rotated normalized vector $p _ { i , 1 }$ . The vector $p _ { i , 2 }$ satisfies 

$$
p _ {i, 2} ^ {\top} p _ {i, 2} = p _ {i, 1} ^ {\top} S _ {1 2} \left(\lambda_ {i} I _ {T - K - 1} - S _ {2 2}\right) ^ {- 2} S _ {2 1} p _ {i, 1}
$$

$$
= p _ {i, 1} ^ {\top} \frac {1}{T} U _ {1} ^ {\top} W \left(F \Lambda^ {T} + e\right) \left(e ^ {\top} W U _ {2} \left(\lambda_ {i} I _ {T - K - 1} - S _ {2 2}\right) ^ {- 2} U _ {2} ^ {\top} W e\right) \left(F \Lambda^ {T} + e\right) ^ {\top} W U _ {1} p _ {i, 1}.
$$

By similar arguments as in the first part of the proof showing the convergence of $\kappa _ { T } ( \lambda )$ it follows that 

$$
\frac {1}{T} U _ {1} ^ {\top} W \left(F \Lambda^ {T}\right) \left(e ^ {\top} W U _ {2} \left(\lambda_ {i} I _ {T - K - 1} - S _ {2 2}\right) ^ {- 2} U _ {2} ^ {\top} W e\right) \left(F \Lambda^ {T}\right) ^ {\top} W U _ {1} = \left(U _ {1} ^ {\top} W F F ^ {\top} W U _ {1}\right) B (\lambda_ {i}) + o _ {p} (1)
$$

$$
\frac {1}{T} U _ {1} ^ {\top} W F \Lambda^ {T} \left(e ^ {\top} W U _ {2} \left(\lambda_ {i} I _ {T - K - 1} - S _ {2 2}\right) ^ {- 2} U _ {2} ^ {\top} W e\right) e ^ {\top} W U _ {1} = o _ {p} (1)
$$

$$
\frac {1}{T} U _ {1} ^ {\top} W e \left(e ^ {\top} W U _ {2} \left(\lambda_ {i} I _ {T - K - 1} - S _ {2 2}\right) ^ {- 2} U _ {2} ^ {\top} W e\right) e ^ {\top} W U _ {1} = \left(U _ {1} ^ {\top} W U _ {1}\right) \frac {c}{N} \text {trace} \left(\Sigma e ^ {\top} \left(\lambda I _ {T} - \frac {1}{T} e e ^ {\top}\right) ^ {- 2} e\right) + o _ {p} (1).
$$

We use the upper bound which is proportional to $B ( \lambda )$ for the last term and apply the rotation $\bar { U } _ { B }$ to diagonalize the signal matrix $M _ { \mathrm { R P - P C A } , B }$ . Therefore, $\| p _ { i , 2 } \| ^ { 2 }$ is asymptotically bounded by 

$$
p _ {i, 2} ^ {\top} p _ {i, 2} \leq p _ {i, 1} ^ {\top} \left( \begin{array}{c c c} \bar {\theta} _ {1, B} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & \bar {\theta} _ {K + 1, B} \end{array} \right) p _ {i, 1} B (\lambda_ {i}) + o _ {p} (1).
$$

This implies 

$$
1 = \| p _ {i, 1} \| ^ {2} + \| p _ {i, 2} \| ^ {2} \leq \| p _ {i, 1} \| ^ {2} (1 + \bar {\theta} _ {i, B} B (\lambda_ {i})) + o _ {p} (1) \leq \| p _ {i, 1} \| ^ {2} (1 + \bar {\theta} _ {i, B} B (G ^ {- 1} (1 / \underline {{\theta}} _ {i, G}))) + o _ {p} (1),
$$

where we have used that ∂B(λ)∂λ < 0 for λ > b. Hence, ∥pi,1∥2 ≥ 11+θ¯i,BB(G−1(1/θ )) . $\begin{array} { r } { \frac { \partial B ( \lambda ) } { \partial \lambda } < 0 } \end{array}$ a $\lambda > b$ $\begin{array} { r } { \| p _ { i , 1 } \| ^ { 2 } \geq \frac { 1 } { 1 + \bar { \theta } _ { i , B } B ( G ^ { - 1 } ( 1 / \underline { { \theta } } _ { i } ) ) } } \end{array}$ We define $\tilde { \rho } _ { i } = \lVert p _ { i , 1 } \rVert$ and its lower bound iρi := 11+θ¯i,BB(G−1(1/θi)) ≤ ˜ρi. Next, we turn to the correlation between the estimated and population factor, which follows $\begin{array} { r } { \underline { { \rho } } _ { i } : = \frac { 1 } { 1 + \bar { \theta } _ { i , B } B ( G ^ { - 1 } ( 1 / \underline { { \theta } } _ { i } ) ) } \le \tilde { \rho } _ { i } } \end{array}$ from similar arguments as in the case $\Sigma = \sigma _ { e } ^ { 2 } I _ { N }$ : 

$$
\begin{array}{l} \left(\frac {1}{T} F ^ {\top} M _ {1} F\right) ^ {- 1 / 2} \left(\frac {1}{T} F ^ {\top} M _ {1} \hat {F}\right) \\ = \left(\frac {1}{T} F ^ {\top} M _ {1} F\right) ^ {- 1 / 2} \left(\left(\left(\frac {1}{T} F ^ {\top} M _ {1} F \left(\frac {1}{T} F ^ {\top} M _ {1} F\right) ^ {- 1 / 2} \quad 0 _ {K \times 1}\right) \bar {U} _ {B} \quad \frac {1}{\sqrt {T}} F ^ {\top} M _ {1} U _ {2}\right) P \hat {D} _ {K} ^ {1 / 2}\right) \\ = \left(\frac {1}{T} F ^ {\top} M _ {1} F\right) ^ {- 1 / 2} \left(\left(\left(\frac {1}{T} F ^ {\top} M _ {1} F \left(\frac {1}{T} F ^ {\top} M _ {1} F\right) ^ {- 1 / 2} \quad 0 _ {K \times 1}\right) \bar {U} _ {B} \quad 0\right) P \hat {D} _ {K} ^ {1 / 2}\right) \\ = \left( \begin{array}{c c} I _ {K} & 0 _ {K \times 1} \end{array} \right) \bar {U} _ {B} P _ {1} \hat {D} _ {K} ^ {1 / 2} \\ = \left( \begin{array}{c c} I _ {K} & 0 _ {K \times 1} \end{array} \right) V \left( \begin{array}{c c c} \tilde {\rho} _ {1} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & \tilde {\rho} _ {K} \end{array} \right) \hat {D} _ {K} ^ {1 / 2}. \\ \end{array}
$$

and 

$$
\begin{array}{l} \frac {1}{T} \hat {F} M _ {1} \hat {F} = \hat {D} _ {K} ^ {1 / 2} P ^ {\top} U ^ {\top} W ^ {- 1} M _ {1} W ^ {- 1} U P \hat {D} _ {K} ^ {1 / 2} \\ = \hat {D} _ {K} ^ {1 / 2} P ^ {\top} U ^ {\top} M _ {1} U P \hat {D} _ {K} ^ {1 / 2} \\ = \hat {D} _ {K} ^ {1 / 2} \left(\left( \begin{array}{c c c} \tilde {\rho} _ {1} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & \tilde {\rho} _ {K} \end{array} \right) V ^ {\top} \left( \begin{array}{c c} I _ {K} & 0 _ {K \times 1} \\ 0 _ {1 \times K} & 0 \end{array} \right) V \left( \begin{array}{c c c} \tilde {\rho} _ {1} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & \tilde {\rho} _ {K} \end{array} \right) \right. \\ + I _ {K} - \left( \begin{array}{c c c} \tilde {\rho} _ {1} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & \tilde {\rho} _ {K} \end{array} \right) V ^ {\top} V \left( \begin{array}{c c c} \tilde {\rho} _ {1} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & \tilde {\rho} _ {K} \end{array} \right) \Bigg) \hat {D} _ {K} ^ {1 / 2}. \\ \end{array}
$$

The result for $\tilde { Q }$ and $\tilde { R }$ follows from this. 

Proof of Corollary 2. Plugging the eigenvalues and eigenvector formulas into Theorem 2 yields: 

$$
\widehat {\mathrm{Corr}} (F, \hat {F}) \stackrel {{p}} {{\to}} \left( \begin{array}{c c} 1 & 0 \end{array} \right) \tilde {U} \binom{\rho_ {1}}{0} \hat {\theta} _ {1} ^ {1 / 2} \widehat {\mathrm{Var}} (\hat {F}) ^ {1 / 2}
$$

$$
\widehat {\operatorname{Var}} (\hat {F}) \xrightarrow {p} \hat {\theta} _ {1} \left(\tilde {U} _ {1, 1} ^ {2} \| u _ {1, 1} \| ^ {2} + \| u _ {1, 2} \| ^ {2}\right)
$$

$$
\hat {\mu} ^ {2} \xrightarrow {p} \frac {1}{1 + \gamma} \tilde {U} _ {1, 2} ^ {2} \rho_ {1} \hat {\theta} _ {1}.
$$

The proof for the limit for $\gamma \to \infty$ is based on the insight that 

$$
\lim _ {\theta \to \infty} B (\theta) \theta^ {2} \to c \sigma_ {e} ^ {2}.
$$

# Appendix C. Supplementary data

Supplementary material related to this article can be found online at https://doi.org/10.1016/j.jeconom.2019.08.012. 

# References



Ahn, S.C., Horenstein, A.R., 2013. Eigenvalue ratio test for the number of factors. Econometrica 81, 1203–1227. 





Aït-Sahalia, Y., Xiu, D., 2017. Principal component estimation of a large covariance matrix with high-frequency data. J. Econometrics 201, 384–399. 





Bai, J., 2003. Inferential theory for factor models of large dimensions. Econometrica 71, 135–171. 





Bai, J., Ng, S., 2002. Determining the number of factors in approximate factor models. Econometrica 70, 191–221. 





Bai, J., Ng, S., 2008. Large dimensional factor analysis. Found. Trends Econom. 3 (2), 89–163. 





Bai, J., Ng, S., 2017. Principal Components and Regularized Estimation of Factor Models. Working Paper. 





Bai, Z., Silverstein, J., 2010. Spectral Analysis of Large Dimensional Random Matrices, second ed. Springer. 





Benaych-Georges, F., Nadakuditi, R.R., 2011. The eigenvalues and eigenvectors of finite, low rank perturbations of large random matrices. Adv. Math. 227, 494–521. 





Bickel, P., Levina, E., 2008. Regularized estimation of large covariance matrices. Ann. Statist. 36 (1), 199–227. 





Bryzgalova, S., 2017. Spurious Factors in Linear Asset Pricing Models. Technical report, Stanford University. 





Chamberlain, G., Rothschild, M., 1983. Arbitrage, factor structure, and mean-variance analysis on large asset markets. Econometrica 51, 1281–1304. 





Connor, G., Korajczyk, R., 1988. Risk and return in an equilibrium apt: Application to a new test methodology. J. Financ. Econ. 21, 255–289. 





Connor, G., Korajczyk, R., 1993. A test for the number of factors in an approximate factor model. J. Finance 58, 1263–1291. 





Fan, J., Liao, Y., Mincheva, M., 2013. Large covariance estimation by thresholding principal orthogonal complements. J. R. Stat. Soc. 75 (4), 603–680. 





Fan, J., Liao, Y., Wang, W., 2016. Projected principal component analysis in factor models. Ann. Statist. 44 (1), 219–254. 





Fan, J., Zhong, Y., 2018. Optimal Subspace Estimation Using Overidentifying Vectors via Generalized Method of Moments. Working Paper. 





Forni, M., Hallin, M., Lippi, M., Reichlin, L., 2000. The generalized dynamic-factor model: Identification and estimation. Review 82, 540–554. 





Harding, M., 2013. Estimating the Number of Factors in Large Dimensional Factor Models. Working paper. 





Harvey, C., Liu, Y., Zhu, H., 2016. ... and the cross-section of expected returns.. Rev. Financ. Stud. 29 (1), 5–68. 





Kelly, B., Pruitt, S., Su, Y., 2017. Instrumented Principal Component Analysis. Working Paper. 





Kozak, S., Nagel, S., Santosh, S., 2018. Shrinking the cross section. J. Financ. Econ. forthcoming. 





Lettau, M., Pelger, M., 2020. Factors that fit the time series and cross-section of stock returns. Rev. Financ. Stud. forthcoming. 





Ludvigson, S., Ng, S., 2010. A Factor Analysis of Bond Risk Premia. Handbook of the Economics of Finance. 





Lütkepohl, H., 1996. Handbook of Matrices. John Wiley & Sons. 





McLean, R., Pontiff, J., 2016. Does academic research destroy stock return predictability?. J. Finance 71 (1), 5–32. 





Nadakuditi, R.R., 2014. Optshrink: An algorithm for improved low-rank signal matrix denoising by optimal, data-driven singular value shrinkage. IEEE Trans. Inform. Theory 60 (5). 





Novy-Marx, R., Velikov, M., 2016. A taxonomy of anomalies and their trading costs. Rev. Financ. Stud. 29, 104–147. 





Onatski, A., 2010. Determining the number of factors from empirical distribution of eigenvalues. Rev. Econ. Stat. 92, 1004–1016. 





Onatski, A., 2012. Asymptotics of the principal components estimator of large factor models with weakly influential factors. J. Econometrics (168), 244–258. 





Paul, D., 2007. Asymptotics of sample eigenstructure for a large dimensional spiked covariance model. Statist. Sinica 17 (4), 1617–1642. 





Pelger, M., 2019. Large-dimensional factor modeling based on high-frequency observations large-dimensional factor modeling based on high-frequency observations. J. Econometrics 208 (1), 23–42. 





Ross, S.A., 1976. The arbitrage theory of capital asset pricing. J. Econom. Theory 13, 341–360. 





Stock, J., Watson, M., 2006. Macroeconomic Forecasting Using Many Predictors. Handbook of Economic Forecasting. North Holland.. 





Yao, J., Zheng, S., Bai, Z., 2015. Large Sample Covariance Matrices and High-Dimensional Data Analysis. Cambridge University Press. 

