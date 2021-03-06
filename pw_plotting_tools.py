#Module for plotting functions to tidy code up
# I think you will need to change some parameters depending on which planet
# you want to plot out. I think these can replace the plotting in the
# main functions if you want to


#Personalised plotting function by me for me just to quickly check on things
def plot_me_quick(x,y,xlabel,ylabel,grid):
    import matplotlib.pyplot as pl
    pl.plot(x,y)
    pl.ylabel(ylabel)
    pl.xlabel(xlabel)
    pl.grid(grid) 
    
 
    #plot specifically for results
def results_plot(z,num_ion,e_charge,E,ion_dict,electron_dict,ac,ag,e_flux,ion_flux):
    import matplotlib.pyplot as pl
    pl.figure(figsize=(8,10))
    pl.subplot(4,2,1)
    plot_me_quick(z/1000,E,'Distance Along Field Line (km)','E Parallel (V/m)','on')
    
    pl.subplot(4,2,2)
    plot_me_quick(z/1000,electron_dict["n"][2:-2,-1],'Distance Along Field Line (km)','Number Density (/m^3)','on')
    for i in range(1,num_ion+1):
        plot_me_quick(z/1000,ion_dict[i]["n"][2:-2,-1],'Distance Along Field Line (km)','Number Density (/m^3)','on')
    pl.yscale('log')
    
    pl.subplot(4,2,3)
    for j in range(1,num_ion+1):
        plot_me_quick(z/1000,ion_dict[j]["T"][2:-2,-1],'Distance Along Field Line (km)','Temperature (K)','on')
        
    pl.subplot(4,2,4)
    for k in range(1,num_ion+1):
        plot_me_quick(z/1000,(e_charge/ion_dict[k]["mass"])*E,'Distance Along Field Line (km)','Acceleration Terms \n(m s^-2)','on')
    plot_me_quick(z/1000,ac,'Distance Along Field Line (km)','Acceleration Terms \n(m s^-2)','on')
    plot_me_quick(z/1000,ag,'Distance Along Field Line (km)','Acceleration Terms \n(m s^-2)','on')  
        
    pl.subplot(4,2,5)
    plot_me_quick(z/1000,e_flux[2:-2,-1],'Distance Along Field Line (km)','Electron Flux \n(m^-2 s^-1) x A (m^2) ','on')
    
    for k in range(1,num_ion+1):
        pl.subplot(4,2,k+5)
        plot_me_quick(z/1000,ion_flux[2:-2,-1,k-1],'Distance Along Field Line (km)','%s Flux \n(m^-2 s^-1)x A (m^2)' %(ion_dict[k]["name"]),'on')
    
    pl.subplots_adjust(hspace=0.5,wspace=0.5)
    pl.suptitle("Results")

def species_plot(z,z_ext,ion_dict,radius):
    import matplotlib.pyplot as pl
    pl.figure(figsize=(15,8))
    ax1 = pl.subplot(2,2,1)
    pl.yscale('log')
    pl.plot(z/1000,ion_dict["n"][2:-2,-1])
    pl.ylabel('Density (kg/m^3)')
    pl.xlabel('Distance Along Field Line (km)')
    pl.xlim([0,z_ext[-1]/1000])
    pl.grid('on') 
    ax2 = ax1.twiny()
    ax2.plot(z/radius,ion_dict["n"][2:-2,-1])
    ax2.set_xlabel('Distance Along Field Line \n (Planetary Radii)')
    ax2.set_xlim([0,z_ext[-1]/radius])
    
    ax3 =pl.subplot(2,2,2)
    pl.plot(z/1000,ion_dict["u"][2:-2,-1])
    pl.ylabel('Velocity (m/s)')
    pl.xlabel('Distance Along Field Line (km)')
    pl.xlim([0,z_ext[-1]/1000])
    pl.grid('on') 
    ax6 = ax3.twiny()
    ax6.plot(z/radius,ion_dict["u"][2:-2,-1])
    ax6.set_xlabel('Distance Along Field Line \n (Planetary Radii)')
    ax6.set_xlim([0,z_ext[-1]/radius])

    
    ax4=pl.subplot(2,2,3)
    pl.plot(z/1000,ion_dict["P"][2:-2,-1])
    pl.ylabel('Pressure (N/m^2)')
    pl.xlabel('Distance Along Field Line (km)')
    pl.xlim([0,z_ext[-1]/1000])
    pl.grid('on') 
    ax7 = ax4.twiny()
    ax7.plot(z/radius,ion_dict["P"][2:-2,-1])
    ax7.set_xlabel('Distance Along Field Line \n (Planetary Radii)')
    ax7.set_xlim([0,z_ext[-1]/radius])
    pl.yscale('log')
    
    ax5=pl.subplot(2,2,4)
    pl.plot(z/1000,ion_dict["T"][2:-2,-1])
    pl.ylabel('Temperature (K)')
    pl.xlabel('Distance Along Field Line (km)')
    pl.xlim([0,z_ext[-1]/1000])
    pl.grid('on') 
    ax8 = ax5.twiny()
    ax8.plot(z/radius,ion_dict["T"][2:-2,-1])
    ax8.set_xlabel('Distance Along Field Line \n (Planetary Radii)')
    ax8.set_xlim([0,z_ext[-1]/radius])
 
    pl.suptitle(ion_dict["name"])
    pl.subplots_adjust(wspace=0.5, hspace=0.5)  
    
def input_plot(ions,electrons,neutrals,z,z_ext,A,radius):
    import matplotlib.pyplot as pl
    
    #length of arrays
    num_ion = len(ions)
    num_neut = len(neutrals)
    
    # Blue = ions
    bl = [0,0.3,0.6],[0,0.4,0.8],[0,0.5,1],[0.2,0.6,1],[0.4,0.7,1],[0.6,0.8,1],[0.8,0.9,1]
    # Green = electrons
    gr = [0.2,1,0.2]
    # Red = neutrals
    rd = [0.6,0,0],[0.8,0,0],[1,0,0],[1,0.2,0.2],[1,0.4,0.4],[1,0.6,0.6],[1,0.8,0.8]
    
    fig = pl.figure(figsize=(8,10))
    ax1 = fig.add_subplot(4,2,1)
    ax1.plot(z/1000,A[2:-2],color=[0,0,0])
    ax1.set_xlim([0,z_ext[-1]/1000])
    ax1.set_xlabel([])
    ax1.xaxis.set_ticklabels([])
    ax1.set_ylabel('Cross-sectional Area \n A (m^2)')
    ax1.grid('on')
    ax2 = ax1.twiny()
    ax2.plot(z/radius,A[2:-2],color=[0,0,0])
    ax2.set_xlabel('Distance Along Field Line \n (Planetary Radii)')
    ax2.set_xlim([0,z_ext[-1]/radius])

    
    ax3 = fig.add_subplot(4,2,2)
    for b in range(1,num_ion+1):
        ax3.plot(z/1000,ions[b]["u"][2:-2,0],color=bl[b])    
    ax3.plot(z/1000,electrons["u"][2:-2,0],color=gr)
    ax3.set_ylabel('Initial Velocity (m/s)')
    ax3.set_xlabel([])
    ax3.xaxis.set_ticklabels([])
    ax3.set_xlim([0,z_ext[-1]/1000])
    ax3.grid('on')
    ax4 = ax3.twiny()
    ax4.plot(z/1000,electrons["u"][2:-2,0],color=gr)
    ax4.set_xlabel('Distance Along Field Line \n (Planetary Radii)')
    ax4.set_xlim([0,z_ext[-1]/radius]) 
    
    
    ax5 = pl.subplot(4,2,3)
    for c in range(1,num_ion+1):
        pl.plot(z/1000,ions[c]["n"][2:-2,0],color=bl[c])    
    pl.plot(z/1000,electrons["n"][2:-2,0],color=gr)
    for d in range(1,num_neut+1):
        pl.plot(z/1000,neutrals[d]["n"][2:-2],color=rd[d])
    pl.ylabel('Initial Number \n Density (m^-3)')
    pl.xlabel([])
    ax5.xaxis.set_ticklabels([])
    pl.xlim([0,z_ext[-1]/1000])
    pl.grid('on')  
    pl.yscale('log')
    
    ax6 = pl.subplot(4,2,4)
    for f in range(1,num_ion+1):
        pl.plot(z/1000,ions[f]["rho"][2:-2,0],color=bl[f]) 
    pl.plot(z/1000,electrons["rho"][2:-2,0],color=gr)
    for h in range(1,num_neut+1):
        pl.plot(z/1000,neutrals[h]["rho"][2:-2],color=rd[h]) 
    pl.ylabel('Initial Mass \n Density (m^-3)')
    pl.xlabel([])
    ax6.xaxis.set_ticklabels([])
    pl.xlim([0,z_ext[-1]/1000])
    pl.grid('on') 
    pl.yscale('log')
    
    ax7 = pl.subplot(4,2,5)
    for i in range(1,num_ion+1):
        pl.plot(z/1000,ions[i]["S"][2:-2],color=bl[i])
    pl.plot(z/1000,electrons["S"][2:-2],color=gr)    
    pl.ylabel('Mass Production Rate \n (kg m^-3 s^-1)')
    pl.xlabel([])
    ax7.xaxis.set_ticklabels([])
    pl.xlim([0,z_ext[-1]/1000])
    pl.grid('on')  
    pl.yscale('log')
    
    
    ax8=pl.subplot(4,2,6)
    for j in range(1,num_ion+1):
        pl.plot(z/1000,ions[j]["T"][2:-2,0],color=bl[j])
    pl.plot(z/1000,electrons["T"][2:-2,0],color=gr)
    pl.plot(z/1000,neutrals[1]["T"][2:-2],color=rd[1]) #all neutrals have same temp
    pl.ylabel('Temperature (K)')
    pl.xlabel([])
    ax8.xaxis.set_ticklabels([])
    pl.xlim([0,z_ext[-1]/1000])
    pl.grid('on') 
    
    pl.subplot(4,2,7)
    for k in range(1,num_ion+1):
        pl.plot(z/1000,ions[k]["P"][2:-2,0],color=bl[k])
    pl.plot(z/1000,electrons["P"][2:-2,0],color=gr)
    pl.plot(z/1000,neutrals[1]["P"][2:-2],color=rd[1]) # same temp same pressure
    pl.ylabel('Pressure (N/m^2)')
    pl.xlabel('Distance Along Field Line (km)')
    pl.yscale('log')
    pl.xlim([0,z_ext[-1]/1000])
    pl.grid('on')    
    
    
    pl.subplot(4,2,8)
    for l in range(1,num_ion+1):
        pl.plot(z/1000,ions[l]["kappa"][2:-2,0],color=bl[l])
    pl.plot(z/1000,electrons["kappa"][2:-2,0],color=gr)
    pl.ylabel('Heat Conductivity \n (J m-1 s-1 K-1)')
    pl.xlabel('Distance Along Field Line (km)')
    pl.xlim([0,z_ext[-1]/1000])
    pl.grid('on')   
    
    
    pl.subplots_adjust(wspace=0.5, hspace=0.0)  
    pl.suptitle("Input")  
    
def plot_single(z,z_ext,item,radius,item_str):
    import matplotlib.pyplot as pl
    ax1 = pl.subplot(1,1,1)
    ax1.plot(z/1000,item,color=[0,0,0])
    ax1.set_xlim([0,z_ext[-1]/1000])
    ax1.set_xlabel('Distance Along Field Line (km)')
    ax1.set_ylabel(item_str)
    ax1.grid('on')
    ax2 = ax1.twiny()
    ax2.plot(z/radius,item,color=[0,0,0])
    ax2.set_xlabel('Distance Along Field Line \n (Planetary Radii)')
    ax2.set_xlim([0,z_ext[-1]/radius])
