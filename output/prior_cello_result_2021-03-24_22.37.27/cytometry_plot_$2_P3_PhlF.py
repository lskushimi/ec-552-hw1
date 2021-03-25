import matplotlib.pyplot as plt
import numpy as np

num_plots = 4

fig, ax = plt.subplots(num_plots, 1, sharex=True, sharey=True)
fig.set_size_inches(4, 1*num_plots)

fig.suptitle("$2 / P3_PhlF")

for a in ax:
    a.set_xscale('log')
    a.set_yscale('log')
    a.set_xlim(1.000000e-03, 1.000000e+02)

ax[0].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [9.322369e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.322369e-06,1.504079e-06,1.504079e-06,0.000000e+00,0.000000e+00,1.504079e-06,1.504079e-06,1.504079e-06,0.000000e+00,0.000000e+00,0.000000e+00,1.504079e-06,0.000000e+00,0.000000e+00,9.322369e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.322369e-06,0.000000e+00,1.504079e-06,0.000000e+00,3.008158e-06,1.864474e-05,1.383461e-05,0.000000e+00,3.008158e-06,0.000000e+00,0.000000e+00,1.864474e-05,0.000000e+00,1.082645e-05,1.082645e-05,0.000000e+00,1.504079e-06,3.008158e-06,9.322369e-06,2.014882e-05,2.315698e-05,9.322369e-06,3.008158e-06,1.504079e-06,9.322369e-06,2.014882e-05,1.383461e-05,9.322369e-06,2.947119e-05,0.000000e+00,4.811592e-05,2.616513e-05,1.233053e-05,3.008158e-06,4.962000e-05,3.247934e-05,4.029763e-05,1.233053e-05,2.616513e-05,1.533869e-05,3.008158e-06,5.563632e-05,1.834684e-05,6.044645e-05,3.247934e-05,6.495869e-05,6.345461e-05,3.398342e-05,4.480987e-05,5.894237e-05,4.480987e-05,2.766921e-05,6.676066e-05,5.413224e-05,3.247934e-05,3.247934e-05,6.495869e-05,1.193888e-04,8.029737e-05,5.563632e-05,1.085624e-04,5.082619e-05,1.100665e-04,5.563632e-05,6.495869e-05,9.743803e-05,1.470580e-04,1.022482e-04,6.495869e-05,8.661159e-05,5.563632e-05,7.097501e-05,6.315672e-05,1.067604e-04,5.714040e-05,7.879330e-05,5.864448e-05,1.473559e-04,9.112382e-05,6.646277e-05,1.332234e-04,7.909119e-05,3.548750e-05,7.520396e-06,1.684276e-05,3.097527e-05,1.533869e-05,6.044645e-05,4.180171e-05,4.811592e-05,4.029763e-05,3.728948e-05,2.014882e-05,1.504079e-06,1.864474e-05,3.247934e-05,1.082645e-05,1.864474e-05,1.504079e-06,3.548750e-05,1.504079e-06,3.728948e-05,2.165290e-05,1.233053e-05,2.315698e-05,2.766921e-05,4.512237e-06,6.016316e-06,2.165290e-05,1.864474e-05,2.165290e-05,2.796711e-05,1.504079e-06,2.014882e-05,0.000000e+00,2.947119e-05,2.165290e-05,2.014882e-05,2.014882e-05,1.504079e-06,9.322369e-06,2.766921e-05,1.383461e-05,2.165290e-05,2.796711e-05,9.322369e-06,4.180171e-05,1.233053e-05,2.616513e-05,2.165290e-05,2.315698e-05,2.014882e-05,3.008158e-06,3.218145e-05,1.052855e-05,1.563804e-04,1.795374e-04,2.841979e-04,5.283961e-04,8.598016e-04,1.379173e-03,2.386048e-03,3.638609e-03,5.497184e-03,8.307861e-03,1.136667e-02,1.578235e-02,2.065282e-02,2.647026e-02,3.328890e-02,3.877184e-02,4.516374e-02,5.239362e-02,5.425645e-02,5.808085e-02,6.046023e-02,6.037630e-02,5.805615e-02,5.635154e-02,5.181349e-02,4.785058e-02,4.295853e-02,3.742554e-02,3.188002e-02,2.655220e-02,2.192268e-02,1.835656e-02,1.520939e-02,1.266971e-02,1.101861e-02,8.895468e-03,7.552988e-03,6.540708e-03,5.275816e-03,4.606974e-03,4.050610e-03,3.504463e-03,2.835636e-03,2.641058e-03,2.047420e-03,1.758397e-03,1.540066e-03,1.271207e-03,1.346084e-03,9.803967e-04,1.010166e-03,1.039637e-03,8.588934e-04,7.271740e-04,5.837345e-04,5.656856e-04,4.607271e-04,3.864461e-04,4.625291e-04,2.763796e-04,3.091569e-04,1.996862e-04,1.819498e-04,2.057025e-04,1.560825e-04,8.661159e-05,1.082645e-04,8.631369e-05,5.864448e-05,5.533843e-05,3.548750e-05,5.563632e-05,6.044645e-05,6.976882e-05,5.262816e-05,1.864474e-05,1.233053e-05,3.008158e-06,1.383461e-05,3.008158e-06,2.947119e-05,1.504079e-06,0.000000e+00,2.014882e-05,9.322369e-06,1.504079e-06,1.082645e-05,9.322369e-06,0.000000e+00,1.082645e-05,])
ax[1].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [9.322369e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.322369e-06,1.504079e-06,1.504079e-06,0.000000e+00,0.000000e+00,1.504079e-06,1.504079e-06,1.504079e-06,0.000000e+00,0.000000e+00,0.000000e+00,1.504079e-06,0.000000e+00,0.000000e+00,9.322369e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.322369e-06,0.000000e+00,1.504079e-06,0.000000e+00,3.008158e-06,1.864474e-05,1.383461e-05,0.000000e+00,3.008158e-06,0.000000e+00,0.000000e+00,1.864474e-05,0.000000e+00,1.082645e-05,1.082645e-05,0.000000e+00,1.504079e-06,3.008158e-06,9.322369e-06,2.014882e-05,2.315698e-05,9.322369e-06,3.008158e-06,1.504079e-06,9.322369e-06,2.014882e-05,1.383461e-05,9.322369e-06,2.947119e-05,0.000000e+00,4.811592e-05,2.616513e-05,1.233053e-05,3.008158e-06,4.962000e-05,3.247934e-05,4.029763e-05,1.233053e-05,2.616513e-05,1.533869e-05,3.008158e-06,5.563632e-05,1.834684e-05,6.044645e-05,3.247934e-05,6.495869e-05,6.345461e-05,3.398342e-05,4.480987e-05,5.894237e-05,4.480987e-05,2.766921e-05,6.676066e-05,5.413224e-05,3.247934e-05,3.247934e-05,6.495869e-05,1.193888e-04,8.029737e-05,5.563632e-05,1.085624e-04,5.082619e-05,1.100665e-04,5.563632e-05,6.495869e-05,9.743803e-05,1.470580e-04,1.022482e-04,6.495869e-05,8.661159e-05,5.563632e-05,7.097501e-05,6.315672e-05,1.067604e-04,5.714040e-05,7.879330e-05,5.864448e-05,1.473559e-04,9.112382e-05,6.646277e-05,1.332234e-04,7.909119e-05,3.548750e-05,7.520396e-06,1.684276e-05,3.097527e-05,1.533869e-05,6.044645e-05,4.180171e-05,4.811592e-05,4.029763e-05,3.728948e-05,2.014882e-05,1.504079e-06,1.864474e-05,3.247934e-05,1.082645e-05,1.864474e-05,1.504079e-06,3.548750e-05,1.504079e-06,3.728948e-05,2.165290e-05,1.233053e-05,2.315698e-05,2.766921e-05,4.512237e-06,6.016316e-06,2.165290e-05,1.864474e-05,2.165290e-05,2.796711e-05,1.504079e-06,2.014882e-05,0.000000e+00,2.947119e-05,2.165290e-05,2.014882e-05,2.014882e-05,1.504079e-06,9.322369e-06,2.766921e-05,1.383461e-05,2.165290e-05,2.796711e-05,9.322369e-06,4.180171e-05,1.233053e-05,2.616513e-05,2.165290e-05,2.315698e-05,2.014882e-05,3.008158e-06,3.218145e-05,1.052855e-05,1.563804e-04,1.795374e-04,2.841979e-04,5.283961e-04,8.598016e-04,1.379173e-03,2.386048e-03,3.638609e-03,5.497184e-03,8.307861e-03,1.136667e-02,1.578235e-02,2.065282e-02,2.647026e-02,3.328890e-02,3.877184e-02,4.516374e-02,5.239362e-02,5.425645e-02,5.808085e-02,6.046023e-02,6.037630e-02,5.805615e-02,5.635154e-02,5.181349e-02,4.785058e-02,4.295853e-02,3.742554e-02,3.188002e-02,2.655220e-02,2.192268e-02,1.835656e-02,1.520939e-02,1.266971e-02,1.101861e-02,8.895468e-03,7.552988e-03,6.540708e-03,5.275816e-03,4.606974e-03,4.050610e-03,3.504463e-03,2.835636e-03,2.641058e-03,2.047420e-03,1.758397e-03,1.540066e-03,1.271207e-03,1.346084e-03,9.803967e-04,1.010166e-03,1.039637e-03,8.588934e-04,7.271740e-04,5.837345e-04,5.656856e-04,4.607271e-04,3.864461e-04,4.625291e-04,2.763796e-04,3.091569e-04,1.996862e-04,1.819498e-04,2.057025e-04,1.560825e-04,8.661159e-05,1.082645e-04,8.631369e-05,5.864448e-05,5.533843e-05,3.548750e-05,5.563632e-05,6.044645e-05,6.976882e-05,5.262816e-05,1.864474e-05,1.233053e-05,3.008158e-06,1.383461e-05,3.008158e-06,2.947119e-05,1.504079e-06,0.000000e+00,2.014882e-05,9.322369e-06,1.504079e-06,1.082645e-05,9.322369e-06,0.000000e+00,1.082645e-05,])
ax[2].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [3.699484e-04,3.255546e-04,2.663628e-04,2.071711e-04,3.255546e-04,4.735339e-04,1.923731e-04,6.215132e-04,2.663628e-04,4.735339e-04,7.103008e-04,4.587360e-04,3.995442e-04,5.179277e-04,4.291401e-04,4.143422e-04,6.067153e-04,4.587360e-04,4.883318e-04,5.327256e-04,4.735339e-04,4.883318e-04,5.179277e-04,5.475236e-04,5.623215e-04,9.618657e-04,8.434822e-04,1.154239e-03,1.405804e-03,1.479793e-03,1.361410e-03,1.435400e-03,1.065451e-03,7.250988e-04,8.138864e-04,1.346612e-03,1.598177e-03,1.953327e-03,2.116105e-03,2.397265e-03,1.642571e-03,1.894136e-03,1.923731e-03,2.175296e-03,3.151960e-03,2.811607e-03,2.397265e-03,2.130903e-03,3.018779e-03,3.921453e-03,3.344333e-03,2.959587e-03,3.877059e-03,4.661349e-03,3.240748e-03,4.528168e-03,5.356852e-03,3.921453e-03,5.682407e-03,5.312458e-03,5.859982e-03,6.895837e-03,6.141143e-03,7.295382e-03,7.680128e-03,7.946491e-03,9.293103e-03,7.265786e-03,8.923154e-03,1.040295e-02,1.058052e-02,1.043254e-02,1.137961e-02,1.220830e-02,1.263744e-02,1.340693e-02,1.420602e-02,1.530106e-02,1.604096e-02,1.612975e-02,1.666247e-02,1.945928e-02,1.820146e-02,1.932610e-02,2.166418e-02,2.139781e-02,2.272963e-02,2.312917e-02,2.496412e-02,2.426861e-02,2.460896e-02,2.687305e-02,2.638472e-02,2.740577e-02,2.838244e-02,2.697663e-02,2.725779e-02,2.835284e-02,2.537846e-02,2.583719e-02,2.407624e-02,2.380988e-02,2.240407e-02,2.025837e-02,1.866020e-02,1.581899e-02,1.376208e-02,1.203072e-02,1.099487e-02,8.819569e-03,7.472957e-03,6.081951e-03,4.720541e-03,3.729079e-03,2.856001e-03,2.086509e-03,1.583379e-03,1.361410e-03,9.766637e-04,9.322699e-04,9.766637e-04,9.322699e-04,5.327256e-04,5.771194e-04,5.919174e-04,3.847463e-04,3.403525e-04,3.699484e-04,3.107566e-04,3.551504e-04,2.515649e-04,1.775752e-04,1.923731e-04,1.923731e-04,1.775752e-04,1.035855e-04,2.219690e-04,1.923731e-04,8.878761e-05,7.398967e-05,1.183835e-04,1.331814e-04,1.183835e-04,1.035855e-04,1.331814e-04,7.398967e-05,1.479793e-05,5.919174e-05,4.439380e-05,2.959587e-05,5.919174e-05,4.439380e-05,0.000000e+00,2.959587e-05,5.919174e-05,4.439380e-05,4.439380e-05,7.398967e-05,2.959587e-05,1.479793e-05,0.000000e+00,2.959587e-05,1.479793e-05,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,4.439380e-05,0.000000e+00,0.000000e+00,4.439380e-05,1.479793e-05,0.000000e+00,1.479793e-05,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[3].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [3.699484e-04,3.255546e-04,2.663628e-04,2.071711e-04,3.255546e-04,4.735339e-04,1.923731e-04,6.215132e-04,2.663628e-04,4.735339e-04,7.103008e-04,4.587360e-04,3.995442e-04,5.179277e-04,4.291401e-04,4.143422e-04,6.067153e-04,4.587360e-04,4.883318e-04,5.327256e-04,4.735339e-04,4.883318e-04,5.179277e-04,5.475236e-04,5.623215e-04,9.618657e-04,8.434822e-04,1.154239e-03,1.405804e-03,1.479793e-03,1.361410e-03,1.435400e-03,1.065451e-03,7.250988e-04,8.138864e-04,1.346612e-03,1.598177e-03,1.953327e-03,2.116105e-03,2.397265e-03,1.642571e-03,1.894136e-03,1.923731e-03,2.175296e-03,3.151960e-03,2.811607e-03,2.397265e-03,2.130903e-03,3.018779e-03,3.921453e-03,3.344333e-03,2.959587e-03,3.877059e-03,4.661349e-03,3.240748e-03,4.528168e-03,5.356852e-03,3.921453e-03,5.682407e-03,5.312458e-03,5.859982e-03,6.895837e-03,6.141143e-03,7.295382e-03,7.680128e-03,7.946491e-03,9.293103e-03,7.265786e-03,8.923154e-03,1.040295e-02,1.058052e-02,1.043254e-02,1.137961e-02,1.220830e-02,1.263744e-02,1.340693e-02,1.420602e-02,1.530106e-02,1.604096e-02,1.612975e-02,1.666247e-02,1.945928e-02,1.820146e-02,1.932610e-02,2.166418e-02,2.139781e-02,2.272963e-02,2.312917e-02,2.496412e-02,2.426861e-02,2.460896e-02,2.687305e-02,2.638472e-02,2.740577e-02,2.838244e-02,2.697663e-02,2.725779e-02,2.835284e-02,2.537846e-02,2.583719e-02,2.407624e-02,2.380988e-02,2.240407e-02,2.025837e-02,1.866020e-02,1.581899e-02,1.376208e-02,1.203072e-02,1.099487e-02,8.819569e-03,7.472957e-03,6.081951e-03,4.720541e-03,3.729079e-03,2.856001e-03,2.086509e-03,1.583379e-03,1.361410e-03,9.766637e-04,9.322699e-04,9.766637e-04,9.322699e-04,5.327256e-04,5.771194e-04,5.919174e-04,3.847463e-04,3.403525e-04,3.699484e-04,3.107566e-04,3.551504e-04,2.515649e-04,1.775752e-04,1.923731e-04,1.923731e-04,1.775752e-04,1.035855e-04,2.219690e-04,1.923731e-04,8.878761e-05,7.398967e-05,1.183835e-04,1.331814e-04,1.183835e-04,1.035855e-04,1.331814e-04,7.398967e-05,1.479793e-05,5.919174e-05,4.439380e-05,2.959587e-05,5.919174e-05,4.439380e-05,0.000000e+00,2.959587e-05,5.919174e-05,4.439380e-05,4.439380e-05,7.398967e-05,2.959587e-05,1.479793e-05,0.000000e+00,2.959587e-05,1.479793e-05,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,4.439380e-05,0.000000e+00,0.000000e+00,4.439380e-05,1.479793e-05,0.000000e+00,1.479793e-05,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])


plt.savefig("/root/output/cytometry_plot_$2_P3_PhlF.png", bbox_inches='tight')
