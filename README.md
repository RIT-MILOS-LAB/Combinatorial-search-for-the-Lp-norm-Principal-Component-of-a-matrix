# Lp-quasinorm-Principal-Component-Analysis
Exact and approximate algorithms for solving Lp-quasinorm (*p &le; 1*) Principal Component Analysis: <a href="https://www.codecogs.com/eqnedit.php?latex=\underset{\mathbf&space;q&space;\in&space;\mathbb&space;R^D}{\text{max.}}\|\mathbf&space;X^\top\mathbf&space;q\|_p^p" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\underset{\mathbf&space;q&space;\in&space;\mathbb&space;R^D}{\text{max.}}\|\mathbf&space;X^\top\mathbf&space;q\|_p^p" title="\underset{\mathbf q \in \mathbb R^D}{\text{max.}}\|\mathbf X^\top\mathbf q\|_p^p" /></a>.

-LpPC_exact_exhaustive.py: solves LpPCA exactly by means of combinatorial optimization. LpPC_exact_exhaustive.py implements the algorithm presented in [1].

-LpBF.py: approximates the exact solution to LpPCA by means of optimal single bit-flips. LpBF.py implements the algorithm presented in [2].

----------------------------
[1]  D. G. Chachlakis and P. P. Markopoulos, Combinatorial search for the Lp-norm principal component of a matrix, in Proceedings IEEE Asilomar Conference on Signals, Systems, and Computers (IEEE ACSSC 2019), Pacific Grove, CA, November 2019.
DOI: 10.1109/IEEECONF44664.2019.9048980
Link: https://ieeexplore.ieee.org/document/9048980

[2] D. G. Chachlakis and P. P. Markopoulos, Novel Algorithms for Lp-quasi-norm Principal-Component Analysis, in Proceedings European Signal Processing Conference (EUSIPCO 2020), Amsterdam, NL, January 2021. 
Link: https://www.eurasip.org/Proceedings/Eusipco/Eusipco2020/pdfs/0001045.pdf
