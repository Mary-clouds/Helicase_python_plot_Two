import matplotlib.pyplot as plt

#data to plot
nct =[75]*20
pcc_one = [4.02188300932745E-8, 2.1356115326991E-5, 0.00, 0.01, 0.09, 0.44, 1.77, 5.68, 14.90, 31.29, 52.02, 70.64, 83.49, 91.11, 95.34, 97.65, 98.92, 99.64, 100.06, 100.30]
cya = [0.000168661]*20
pcc_two=[75.00004217]*20

x_achse = list (range(1, 21))
#styling and plotting
plt.plot(x_achse, nct, label ='NCT (n=4)', color = 'b')
plt.plot(x_achse, pcc_one, label ='PCC 7806 (n=1)', color = 'g')
plt.plot(x_achse, cya, label ='CYA 126 (n=1)', color = 'r')
plt.plot(x_achse, pcc_two, label ='PCC 7005 (n=4)', color = 'y')

# fix the x-axis ticks to show integers from 1 to 20
plt.xticks(ticks=range(1, 21), labels=range(1, 21))

# Adjust the layout to prevemt labels from being cut off
plt.tight_layout()

#add label and title
plt.title('with Helicase')
plt.xlabel('Cycles')
plt.ylabel ('dRn')
plt.legend()

#saving the plot as jpg
plt.savefig('with Helicase.jpg', dpi = 400)
#display the plot
plt.show()