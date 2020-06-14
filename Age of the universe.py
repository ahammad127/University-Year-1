import numpy as np
import matplotlib.pyplot as plt
import math as m
import scipy.optimize as opt
'''Beginning of step 1'''

'''This first section is me making an array of the parallax angles and calculating the distances from them'''
parallax = [2.01,2.78,3.14,2.28,3,2.13,3.66,2.81,1.9,2.4]
Parallax = np.array(parallax)
d = 1000/Parallax
D = np.array(d) #I always converted my lists to arrays as I could only carry out mathematical operations using arrays

'''Mew1 is an array of the logarithms of the distances, it is an intermediary for me to calculate the value for Mew'''
mew1 = [m.log10(d[0]),m.log10(d[1]),m.log10(d[2]),m.log10(d[3]),m.log10(d[4]),m.log10(d[5]),m.log10(d[6]),m.log10(d[7]),m.log10(d[8]),m.log10(d[9])]
Mew1 = np.array(mew1)
mew = 5*Mew1-5
Mew = np.array(mew)

'''Av is an array of the values of extinctions in the V-band of the cepheids'''
av = [0.52,0.06,0.25,0.37,0.58,0.67,0.23,0.64,0.34,0.2]
Av = np.array(av)
vdiff = Mew + Av #vdiff is my value for apparent magnitude - absolute magnitude (mv - Mv)
Vdiff = np.array(vdiff)

'''mV is an array of the values of the apparent magnitudes of the cepheids, which I then used to calculate MV, the array of absolute magnitudes'''
mv = [3.732,3.911,3.751,4.667,4.556,5.743,3.96,5.372,5.752,5.464]
mV = np.array(mv)
Mv = Vdiff - mV
MV = -1*np.array(Mv)

'''Lines 27 to 34 is basically repeating what I did in lines 17 to 25 but in the I-band instead of the V-band'''
ai = 0.556*Av
Ai = np.array(ai)
idiff = Mew + Ai
Idiff = np.array(idiff)
mi = [2.557,3.085,2.943,3.862,3.661,4.814,3.204,4.51,5.052,4.778]
mI = np.array(mi)
Mi = Idiff - mI
MI = -1*np.array(Mi)

'''LogP is an array of the logarithms of the periods of the cepheids'''
logP = [m.log10(35.551341),m.log10(10.15073),m.log10(9.842425),m.log10(7.594904),m.log10(7.012877),m.log10(5.77338),m.log10(5.36627),m.log10(4.470916),m.log10(4.435462),m.log10(3.72819)]
LogP = np.array(logP)

'''Lines 39 to 55 are the propagation of errors of all the values I have so far'''
parerr = [0.2,0.18,0.16,0.2,0.18,0.29,0.15,0.18,0.23,0.19]
Parerr = np.array(parerr) #Array of errors in parallax
derr = 1000*Parerr/(Parallax**2)
Derr = np.array(derr) #Array of errors in the distances
mewerr = (Derr/(D*m.log(10)))*5
Mewerr = np.array(mewerr) #Array of errors in Mew
averr = [0.06,0.03,0.05,0.03,0.1,0.04,0.03,0.06,0.06,0.08]
Averr = np.array(averr) #Array of errors of extinction in the V-band
mverr0 = Mewerr**2 + Averr**2 #mverr0 is an intermediary I used to help me calculate the error in absolut magnitude
mverr = [m.sqrt(mverr0[0]),m.sqrt(mverr0[1]),m.sqrt(mverr0[2]),m.sqrt(mverr0[3]),m.sqrt(mverr0[4]),m.sqrt(mverr0[5]),m.sqrt(mverr0[6]),m.sqrt(mverr0[7]),m.sqrt(mverr0[8]),m.sqrt(mverr0[9])]
MVerr = np.array(mverr) #MVerr is an array of the errors for the absolute magnitudes in the V-band

'''Lines 50 to 55 are the errors to do with the I-band'''
aierr = 0.556*Averr
Aierr = np.array(aierr)
mierr0 = Mewerr**2 + Aierr**2
mierr = [m.sqrt(mierr0[0]),m.sqrt(mierr0[1]),m.sqrt(mierr0[2]),m.sqrt(mierr0[3]),m.sqrt(mierr0[4]),m.sqrt(mierr0[5]),m.sqrt(mierr0[6]),m.sqrt(mierr0[7]),m.sqrt(mierr0[8]),m.sqrt(mierr0[9])]
MIerr = np.array(mierr)

'''The function below is to help determine a line of best fit, and a model for what the absolute magnitudes theoretically should be'''
def func(x, slope, intercept):
    line = slope*x+ intercept
    return line

'''The opt.curve_fit function is what will use the func function to produce a gradient, intercept and the errors in them. The x-axis here the logarithm of the period and the y-axis is the absolute magnitude'''
line, matrix = opt.curve_fit(f=func, xdata=LogP, ydata=MV, sigma=MVerr, p0=(0,0), absolute_sigma=True)
alphav = line[0] #The gradient of the slope is ALPHAv, line[0] is the gradient
betav = line[1] #The intercept of the slope is BETAv, line[1] is the intercept
error = np.sqrt(np.diag(matrix)) #The error in intercept and slope is produced as a matrix, but you have to take the sqrt of the diagonal of it to get the actual errors
alphaverr = error[0] #Error in the gradient, and thus error in ALPHAv is error[0]
betaverr = error[1] #Error in the intercept, and thus error in BETAv is error[1]
MVmod = alphav*LogP + betav #MVmod is the model for what the absolute magnitudes should be theoretically

'''Lines 69 to 73 plot the graph of MV against LogP, with error bars and a straight line of best fit'''
plt.plot(LogP,MVmod,color = 'blue', linestyle = '-')
plt.xlabel("Logarithm of the period in days")
plt.ylabel("MV (mag)")
plt.errorbar(LogP, MV, yerr = MVerr, fmt='o')
plt.show()
chi2v = np.sum(((MV-MVmod)**2.0)/(MVerr**2.0)) #This is the chi2 associated with the absolute magnitude
redchi2v = chi2v/8 #This is the reduced chi squared
print "ALPHAv is", alphav, "+ or -", alphaverr
print "BETAv is", betav, "+ or -", betaverr
print "Chi-squared is", chi2v
print "Reduced chi-squared is", redchi2v

'''Line 82 to 100 effectively repeat line 61 to 80 but they are associated with everything in the I-band'''
line, matrix = opt.curve_fit(f=func, xdata=LogP, ydata=MI, sigma=MIerr, p0=(0,0), absolute_sigma=True)
alphai = line[0]
betai = line[1]
error = np.sqrt(np.diag(matrix))
alphaierr = error[0]
betaierr = error[1]
MImod = alphai*LogP + betai
plt.plot(LogP,MImod,color = 'blue', linestyle = '-')
plt.xlabel("Logarithm of the period in days")
plt.ylabel("MI (mag)")
plt.errorbar(LogP, MI, yerr = MIerr, fmt='o')
plt.show()
chi2i = np.sum(((MI-MImod)**2.0)/(MIerr**2.0))
redchi2i = chi2i/8
print "ALPHAi is", alphai, "+ or -", alphaierr
print "BETAi is", betai, "+ or -", betaierr
print "Chi-squared is", chi2i
print "Reduced chi-squared is", redchi2i

'''End of step 1
Beginning of step 2'''
'''logP1, mv1 and mi1 are all arrays of the logarithms of the periods of the cepheids, apparent magnitudes of the cepheids in the V-band and apparent magnitudes of cepheids in the I-band for the first galaxy'''
logP1 = np.array([1.623,1.602,1.342,1.415,1.26,1.431,1.613,1.763,1.415,1.255,1.272,1.407,1.505,1.681,1.452,1.288,1.477,1.431,1.288,1.342,1.288,1.613,1.272,1.415,1.283])
mv1 = np.array([24.55,24.87,24.71,25.03,25.83,25.71,24.24,24.80,24.84,25.19,25.58,25.29,24.64,24.35,25.24,25.77,24.99,25.22,25.01,25.14,25.38,24.21,25.76,25.42,25.47])
mi1 = np.array([23.53,24.05,24.23,24.05,24.99,24.70,23.20,23.86,24.03,24.48,24.61,24.26,23.68,23.28,24.35,24.98,23.98,24.35,24.32,24.24,24.38,23.35,25.17,24.76,24.58])

MV1 = np.array(alphav*logP1 + betav) #MV1 is an array of the absolute magnitudes calculated from the logarithm of the period and the alpha and beta calculated in step 1, for the first galaxy
MV1err = ((alphaverr*logP1)**2 + betaverr**2)**0.5 #MV1err is the error of the absolute magnitudes calculated for the first galaxy
logdv1 = np.array((mv1 - MV1 - 0.0992 + 5)/5) #logdv1 is an array of the logarithm of the distance from each cepheid calculated using the V-band ALPHA and BETA, where 0.0992 is the extinction given associated with this galaxy
logdv1err = MV1err/5 #logdv1err is the errors for logdv1

'''Lines 124 to 127 repeat lines 119 to 122 but in the I-band rather than the V-band'''
MI1 = np.array(alphai*logP1 + betai)
MI1err = ((alphaierr*logP1)**2 + betaierr**2)**0.5
logdi1 = np.array((mi1 - MI1 - 0.0992*0.556 + 5)/5)
logdi1err = MI1err/5

dv1 = 10**logdv1 #dv1 is all of the distances in pc to each cepheid
dv1err = dv1*m.log(10)*logdv1err #dv1err is the error in the distances
DV1 = dv1.mean() #DV1 is the mean of the distances to the cepheids, giving an approximation of the distance to the galaxy using the V-band
DV1err = ((np.array(dv1err**2).sum())**0.5)/len(dv1) #DV1err is the error in DV1

'''Lines 135 to 138 effectively repeat lines 130 to 133 but use everything associated with the I-band rather than the V-band'''
di1 = 10**logdi1
di1err = di1*m.log(10)*logdi1err
DI1 = di1.mean()
DI1err = ((np.array(di1err**2).sum())**0.5)/len(di1)

D1 = (DI1 + DV1)/2 #D1 is the mean of the distances calculated using the V-band and I-band to give an approximation of the distance in pc to the galaxy
D1err = ((DV1err**2+DI1err**2)**0.5)/2 #D1err is the error in D1
print "The distance to galaxy NGC3627 is", D1/1000000, "+ or -", D1err/1000000, "Mpc"
'''Lines 145 to 298 effectively repeat line 114 to 143 but they do the calculations associated with all of the other galaxies, calculating the approximation of the distance to them and the error in that approximation'''

'''Calculations for galaxy 2'''
logP2 = np.array([1.468,1.386,1.633,1.328,1.687,1.449,1.607,1.572,1.400,1.439,1.613,1.330,1.484,1.535,1.320,1.402,1.525])
mv2 = np.array([26.60,26.72,26.86,27.08,26.22,26.35,26.01,26.71,26.77,26.89,24.85,26.94,26.95,26.61,26.86,25.57,25.72])
mi2 = np.array([25.58,25.89,25.78,26.03,25.38,25.65,25.51,25.87,25.58,25.96,24.08,26.11,25.50,25.48,25.74,25.03,24.81])
MV2 = np.array(alphav*logP2 + betav)
MV2err = ((alphaverr*logP2)**2 + betaverr**2)**0.5
logdv2 = np.array((mv2 - MV2 - 0.0434 + 5)/5)
logdv2err = MV2err/5
MI2 = np.array(alphai*logP2 + betai)
MI2err = ((alphaierr*logP2)**2 + betaierr**2)**0.5
logdi2 = np.array((mi2 - MI2 - 0.0434*0.556 + 5)/5)
logdi2err = MI2err/5
dv2 = 10**logdv2
dv2err = dv2*m.log(10)*logdv2err
DV2 = dv2.mean()
DV2err = ((np.array(dv2err**2).sum())**0.5)/len(dv2)
di2 = 10**logdi2
di2err = di2*m.log(10)*logdi2err
DI2 = di2.mean()
DI2err = ((np.array(di2err**2).sum())**0.5)/len(di2)
D2 = (DI2 + DV2)/2
D2err = ((DV2err**2+DI2err**2)**0.5)/2
print "The distance to galaxy NGC3982 is", D2/1000000, "+ or -", D2err/1000000, "Mpc"

'''Calculations for galaxy 3'''
logP3 = np.array([1.511,1.447,1.449,1.294,1.462,1.301,1.653,1.462,1.505,1.352,1.613,1.724,1.602,1.447,1.699,1.716,1.708,1.328,1.255,1.519,1.720,1.720,1.531,1.398,1.663,1.591,1.531,1.283,1.716,1.255,1.845,1.386,1.369,1.281,1.401,1.484,1.436,1.375,1.267,1.412,1.281,1.748,1.556])
mv3 = np.array([25.57,25.86,26.04,26.27,25.70,26.33,24.75,25.42,25.14,26.29,25.63,24.47,25.15,25.39,25.27,25.23,24.44,26.22,26.31,25.26,25.14,24.37,25.49,25.79,25.23,25.45,25.84,26.39,24.50,26.30,24.52,26.07,25.64,26.18,25.49,25.19,25.46,25.58,26.50,25.62,26.42,25.11,25.43])
mi3 = np.array([24.71,25.06,25.29,25.61,24.77,25.41,23.99,24.48,24.34,25.69,24.60,23.60,24.29,24.64,24.38,24.32,23.57,25.56,25.26,24.61,24.18,23.47,24.49,24.94,24.28,24.62,24.99,25.64,23.72,25.46,23.51,25.38,24.98,25.20,24.81,24.47,24.57,24.62,25.58,24.87,25.67,24.06,24.41])
MV3 = np.array(alphav*logP3 + betav)
MV3err = ((alphaverr*logP3)**2 + betaverr**2)**0.5
logdv3 = np.array((mv3 - MV3 - 0.0775 + 5)/5)
logdv3err = MV3err/5
MI3 = np.array(alphai*logP3 + betai)
MI3err = ((alphaierr*logP3)**2 + betaierr**2)**0.5
logdi3 = np.array((mi3 - MI3 - 0.0775*0.556 + 5)/5)
logdi3err = MI3err/5
dv3 = 10**logdv3
dv3err = dv3*m.log(10)*logdv3err
DV3 = dv3.mean()
DV3err = ((np.array(dv3err**2).sum())**0.5)/len(dv3)
di3 = 10**logdi3
di3err = di3*m.log(10)*logdi3err
DI3 = di3.mean()
DI3err = ((np.array(di3err**2).sum())**0.5)/len(di3)
D3 = (DI3 + DV3)/2
D3err = ((DV3err**2+DI3err**2)**0.5)/2
print "The distance to galaxy NGC4496A is", D3/1000000, "+ or -", D3err/1000000, "Mpc"

'''Calculations for galaxy 4'''
logP4 = np.array([1.318,1.312,1.405,1.712,1.310,1.653,1.525,1.590,1.444,1.593,1.763,1.749,1.686,1.377,1.377,1.430,1.346,1.511,1.465,1.430,1.610,1.346])
mv4 = np.array([26.28,25.96,25.61,25.07,26.03,25.04,26.78,25.34,25.88,25.42,24.91,25.18,24.72,26.03,25.83,25.63,25.86,25.50,25.98,25.65,24.88,26.26])
mi4 = np.array([25.44,25.14,24.45,23.68,24.95,24.02,25.15,24.24,24.94,24.40,24.26,23.93,23.67,25.09,24.89,24.67,25.04,24.17,24.62,24.66,23.85,25.10])
MV4 = np.array(alphav*logP4 + betav)
MV4err = ((alphaverr*logP4)**2 + betaverr**2)**0.5
logdv4 = np.array((mv4 - MV4 - 0.0682 + 5)/5)
logdv4err = MV4err/5
MI4 = np.array(alphai*logP4 + betai)
MI4err = ((alphaierr*logP4)**2 + betaierr**2)**0.5
logdi4 = np.array((mi4 - MI4 - 0.0682*0.556 + 5)/5)
logdi4err = MI4err/5
dv4 = 10**logdv4
dv4err = dv4*m.log(10)*logdv4err
DV4 = dv4.mean()
DV4err = ((np.array(dv4err**2).sum())**0.5)/len(dv4)
di4 = 10**logdi4
di4err = di4*m.log(10)*logdi4err
DI4 = di4.mean()
DI4err = ((np.array(di4err**2).sum())**0.5)/len(di4)
D4 = (DI4 + DV4)/2
D4err = ((DV4err**2+DI4err**2)**0.5)/2
print "The distance to galaxy NGC4527 is", D4/1000000, "+ or -", D4err/1000000, "Mpc"

'''Calculations for galaxy 5'''
logP5 = np.array([1.480,1.312,1.505,1.551,1.580,1.458,1.435,1.771,1.763,1.726,1.519,1.327,1.623,1.477,1.490,1.491,1.535,1.813,1.348,1.407,1.364,1.386,1.799,1.562,1.447,1.771,1.458,1.597,1.387,1.699,1.740])
mv5 = np.array([26.04,26.05,25.65,25.75,25.31,25.81,26.00,24.74,25.39,25.12,25.31,26.21,25.61,26.14,25.75,25.93,25.24,24.80,26.06,25.53,25.18,26.00,25.13,25.33,25.55,24.49,25.62,25.60,25.53,25.35,25.44])
mi5 = np.array([24.91,25.35,24.69,24.45,24.30,25.09,25.42,23.90,24.48,24.20,24.46,25.21,24.88,25.34,24.88,25.11,24.57,24.06,24.95,24.77,24.39,25.17,23.85,24.50,24.23,23.43,25.34,24.47,24.88,24.28,24.13])
MV5 = np.array(alphav*logP5 + betav)
MV5err = ((alphaverr*logP5)**2 + betaverr**2)**0.5
logdv5 = np.array((mv5 - MV5 - 0.0558 + 5)/5)
logdv5err = MV5err/5
MI5 = np.array(alphai*logP5 + betai)
MI5err = ((alphaierr*logP5)**2 + betaierr**2)**0.5
logdi5 = np.array((mi5 - MI5 - 0.0558*0.556 + 5)/5)
logdi5err = MI5err/5
dv5 = 10**logdv5
dv5err = dv5*m.log(10)*logdv5err
DV5 = dv5.mean()
DV5err = ((np.array(dv5err**2).sum())**0.5)/len(dv5)
di5 = 10**logdi5
di5err = di5*m.log(10)*logdi5err
DI5 = di5.mean()
DI5err = ((np.array(di5err**2).sum())**0.5)/len(di5)
D5 = (DI5 + DV5)/2
D5err = ((DV5err**2+DI5err**2)**0.5)/2
print "The distance to galaxy NGC4536 is", D5/1000000, "+ or -", D5err/1000000, "Mpc"

'''Calculations for galaxy 6'''
logP6 = np.array([1.473,1.336,1.505,1.613,1.681,1.415,1.477,1.322,1.538,1.531,1.505,1.322,1.602,1.763,1.716])
mv6 = np.array([27.03,26.78,26.14,25.79,25.24,26.67,26.18,26.96,26.72,25.87,26.26,26.28,25.65,26.39,26.01])
mi6 = np.array([25.94,26.09,25.31,24.95,24.48,25.72,25.31,26.02,25.90,25.52,25.52,25.17,25.08,25.36,25.07])
MV6 = np.array(alphav*logP6 + betav)
MV6err = ((alphaverr*logP6)**2 + betaverr**2)**0.5
logdv6 = np.array((mv6 - MV6 - 0.0806 + 5)/5)
logdv6err = MV6err/5
MI6 = np.array(alphai*logP6 + betai)
MI6err = ((alphaierr*logP6)**2 + betaierr**2)**0.5
logdi6 = np.array((mi6 - MI6 - 0.0806*0.556 + 5)/5)
logdi6err = MI6err/5
dv6 = 10**logdv6
dv6err = dv6*m.log(10)*logdv6err
DV6 = dv6.mean()
DV6err = ((np.array(dv6err**2).sum())**0.5)/len(dv6)
di6 = 10**logdi6
di6err = di6*m.log(10)*logdi6err
DI6 = di6.mean()
DI6err = ((np.array(di6err**2).sum())**0.5)/len(di6)
D6 = (DI6 + DV6)/2
D6err = ((DV6err**2+DI6err**2)**0.5)/2
print "The distance to galaxy NGC4639 is", D6/1000000, "+ or -", D6err/1000000, "Mpc"

'''Calculations for galaxy 7'''
logP7 = np.array([0.497,0.431,0.951,0.899,1.066,0.746,1.099,0.983,0.786,0.641,1.137,1.207])
mv7 = np.array([25.25,26.01,24.22,24.39,23.61,24.45,23.65,23.86,24.80,24.68,23.54,23.08])
mi7 = np.array([24.32,25.00,23.31,22.76,23.24,23.47,22.80,23.10,24.06,23.96,22.50,22.55])
MV7 = np.array(alphav*logP7 + betav)
MV7err = ((alphaverr*logP7)**2 + betaverr**2)**0.5
logdv7 = np.array((mv7 - MV7 - 0.1736 + 5)/5)
logdv7err = MV7err/5
MI7 = np.array(alphai*logP7 + betai)
MI7err = ((alphaierr*logP7)**2 + betaierr**2)**0.5
logdi7 = np.array((mi7 - MI7 - 0.1736*0.556 + 5)/5)
logdi7err = MI7err/5
dv7 = 10**logdv7
dv7err = dv7*m.log(10)*logdv7err
DV7 = dv7.mean()
DV7err = ((np.array(dv7err**2).sum())**0.5)/len(dv7)
di7 = 10**logdi7
di7err = di7*m.log(10)*logdi7err
DI7 = di7.mean()
DI7err = ((np.array(di7err**2).sum())**0.5)/len(di7)
D7 = (DI7 + DV7)/2
D7err = ((DV7err**2+DI7err**2)**0.5)/2
print "The distance to galaxy NGC5253 is", D7/1000000, "+ or -", D7err/1000000, "Mpc"

'''Calculations for galaxy 8'''
logP8 = np.array([0.842,0.863,1.393,0.964,1.623,0.760,1.574,0.838,0.629,0.790,1.332,1.021,1.124,1.560,0.565,0.766,0.714,1.568,1.547,0.852,1.255,1.623,1.342,1.314,1.204,0.866,1.428])
mv8 = np.array([24.47,24.54,23.29,24.10,21.87,24.65,22.86,24.57,24.98,25.13,22.80,24.56,24.04,22.36,24.83,24.80,24.85,22.70,22.72,24.65,23.14,22.33,23.42,23.36,23.76,24.85,23.20])
mi8 = np.array([23.71,23.75,22.45,23.55,21.19,23.86,21.85,24.00,24.59,24.63,22.60,23.76,23.28,21.57,24.74,24.43,24.51,21.79,22.17,24.29,22.77,21.40,22.62,22.31,23.11,24.34,22.25])
MV8 = np.array(alphav*logP8 + betav)
MV8err = ((alphaverr*logP8)**2 + betaverr**2)**0.5
logdv8 = np.array((mv8 - MV8 - 0.0434 + 5)/5)
logdv8err = MV8err/5
MI8 = np.array(alphai*logP8 + betai)
MI8err = ((alphaierr*logP8)**2 + betaierr**2)**0.5
logdi8 = np.array((mi8 - MI8 - 0.0434*0.556 + 5)/5)
logdi8err = MI8err/5
dv8 = 10**logdv8
dv8err = dv8*m.log(10)*logdv8err
DV8 = dv8.mean()
DV8err = ((np.array(dv8err**2).sum())**0.5)/len(dv8)
di8 = 10**logdi8
di8err = di8*m.log(10)*logdi8err
DI8 = di8.mean()
DI8err = ((np.array(di8err**2).sum())**0.5)/len(di8)
D8 = (DI8 + DV8)/2
D8err = ((DV8err**2+DI8err**2)**0.5)/2
print "The distance to galaxy IC4182 is", D8/1000000, "+ or -", D8err/1000000, "Mpc"
'''End of step 2
Beginning of steps 3 and 4 (did them in one go)'''

'''Dgal is an array of the distances to the 8 galaxies in Mpc, Dgalerr is the error in Dgal, Vrec is the recessional velocity of each galaxy'''
Dgal = np.array([D1/1000000, D2/1000000, D3/1000000, D4/1000000, D5/1000000, D6/1000000, D7/1000000, D8/1000000])
Dgalerr = np.array([D1err/1000000, D2err/1000000, D3err/1000000, D4err/1000000, D5err/1000000, D6err/1000000, D7err/1000000, D8err/1000000])
Vrec = np.array([427,1510,1152,1152,1152,1152,170,303])

'''Line 322 is the function used to determine the gradient and error in the gradient of a graph of Dgal against Vrec'''
line, matrix = opt.curve_fit(f=func, xdata=Vrec, ydata=Dgal, sigma=Dgalerr, p0=(0,0), absolute_sigma=True)
age = line[0] #The age of the universe is the gradient of the graph, which is line[0]
error = np.sqrt(np.diag(matrix)) #The error in gradient and intercept are outputted as a matrix, where the actual errors are the sqrt of the diagonals of the matrix
agerr = error[0] #The agerr is the error in the age, which is error[0]
DgalMod = Vrec*age + line[1] #DgalMod is the model of what the distances to the galaxies theoretically should be

'''Line 329 to 333 plot a graph of Dgal against Vrec with error bars and a straight line of best fit'''
plt.plot(Vrec, DgalMod, color = 'blue', linestyle = '-')
plt.xlabel("Recessional velocity (km/s)")
plt.ylabel("Distance to the galaxies (Mpc)")
plt.errorbar(Vrec, Dgal, yerr = Dgalerr, fmt='o')
plt.show()

Age = (3.086*(10**19))*age/3600/24/365.25 #This line converts the unit of the age of the universe to years
Agerr = (3.086*(10**19))*agerr/3600/24/365.25 #This line converts the unit of the error of the age of the universe to years
chi2 = np.sum(((Dgal - DgalMod)**2.0)/(Dgalerr**2.0)) #This is the chi2 value for the distances to the galaxies
redchi2 = chi2/6  #This is the reduced chi squared
print "The age of the universe is", Age, "+ or -", Agerr, "years."
print "Chi-squared is", chi2
print "Reduced chi-squared is", redchi2
'''This is just to make sure i submit the right document'''