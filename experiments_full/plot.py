import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

n1 = [np.genfromtxt('n1_c8.results',   unpack=True, skip_footer=1)[5],
      np.genfromtxt('n1_c16.results',  unpack=True, skip_footer=1)[5],
      np.genfromtxt('n1_c32.results',  unpack=True, skip_footer=1)[5],
      np.genfromtxt('n1_c64.results',  unpack=True, skip_footer=1)[5],
      np.genfromtxt('n1_c128.results', unpack=True, skip_footer=1)[5]]
n10 = [np.genfromtxt('n10_c8.results',   unpack=True, skip_footer=1)[5],
       np.genfromtxt('n10_c16.results',  unpack=True, skip_footer=1)[5],
       np.genfromtxt('n10_c32.results',  unpack=True, skip_footer=1)[5],
       np.genfromtxt('n10_c64.results',  unpack=True, skip_footer=1)[5],
       np.genfromtxt('n10_c128.results', unpack=True, skip_footer=1)[5]]
n100 = [np.genfromtxt('n100_c8.results',   unpack=True, skip_footer=1)[5],
       np.genfromtxt('n100_c16.results',  unpack=True, skip_footer=1)[5],
       np.genfromtxt('n100_c32.results',  unpack=True, skip_footer=1)[5],
       np.genfromtxt('n100_c64.results',  unpack=True, skip_footer=1)[5],
       np.genfromtxt('n100_c128.results', unpack=True, skip_footer=1)[5]]

positions = list(map(lambda x: (x*0.15), [8, 16, 32, 64, 128]))
mpl.rcParams["image.cmap"] = "jet"

f, main_axis = plt.subplots()

main_axis.set_yscale('log')
main_axis.set_xscale('log')
# sub_axis = f.add_axes([0.45, 0.45, 0.43, 0.4])
# sub_axis.boxplot(n10, positions=positions, widths=5, notch=True)
# sub_axis.set_xlim(0,150)

means_n1   = list(map(np.mean, n1))
means_n10  = list(map(np.mean, n10))
means_n100 = list(map(np.mean, n100))
l1 = main_axis.errorbar(positions, means_n1, list(map(lambda x: np.sqrt(np.var(x)), n1)), marker="o", label='N = 1')
l2 = main_axis.errorbar(positions, means_n10, list(map(lambda x: np.sqrt(np.var(x)), n10)), marker=">", label='N = 10')
l3 = main_axis.errorbar(positions, means_n100, list(map(lambda x: np.sqrt(np.var(x)), n100)), marker="<", label='N = 100')
main_axis.legend()
main_axis.set_xlabel('cluster diameter (T)')
main_axis.set_ylabel('time to discovery (seconds)')

xs = np.arange(0.15*8,0.15*128,0.001)

def f1(t):
    return (32*(50**2)) / (np.sqrt(t))

def f10(t):
    return (32*(2.0/3.0) * (50**2)) / (10*np.sqrt(t))

def f100(t):
    return (32*(2.0/3.0) * (50**2)) / (100*np.sqrt(t))

main_axis.set_prop_cycle(None)

main_axis.plot(xs, list(map(f1, xs)), linestyle='--')
main_axis.plot(xs, list(map(f10, xs)), linestyle='--')
main_axis.plot(xs, list(map(f100, xs)), linestyle='--')

f.show()
