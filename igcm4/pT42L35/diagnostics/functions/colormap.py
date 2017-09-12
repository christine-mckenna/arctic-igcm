import matplotlib 

def custom_div_cmap_r(numcolors=11, name='custom_div_cmap_r', mincol='darkred', mincol2='orangered',mincol3='gold',midcol='white',maxcol3='lightskyblue',maxcol2='dodgerblue',maxcol='darkblue'):

    from matplotlib.colors import LinearSegmentedColormap

    cmap = LinearSegmentedColormap.from_list(name=name, colors=[mincol,mincol2,mincol3,midcol,maxcol3,maxcol2,maxcol], N=numcolors)

    return cmap

def custom_div_cmap(numcolors=11, name='custom_div_cmap_r', mincol='darkblue', mincol2='dodgerblue',mincol3='lightskyblue',midcol='white',maxcol3='gold',maxcol2='orangered',maxcol='darkred'):

    from matplotlib.colors import LinearSegmentedColormap

    cmap = LinearSegmentedColormap.from_list(name=name, colors=[mincol,mincol2,mincol3,midcol,maxcol3,maxcol2,maxcol], N=numcolors)

    return cmap

def custom_div_cmap_RdBu(numcolors=11, name='custom_div_cmap_r', mincol='steelblue', mincol2='cornflowerblue',mincol3='powderblue',midcol='white',maxcol3='lightsalmon',maxcol2='indianred',maxcol='darkred'):

    from matplotlib.colors import LinearSegmentedColormap

    cmap = LinearSegmentedColormap.from_list(name=name, colors=[mincol,mincol2,mincol3,midcol,maxcol3,maxcol2,maxcol], N=numcolors)

    return cmap
