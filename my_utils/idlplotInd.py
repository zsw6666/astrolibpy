import idlplot

""" 
This module is a set wrappers around idlplot designed to make 
the plots of subsets of the data: e.g.
plot(x,y,ind=ind)
instead of plot(x[ind],y[ind])
  
"""
def tvhist2d(a,b,*args,**kw):
	ind = kw.get('ind')
	
	if ind is None:
		idlplot.tvhist2d(a,b,*args,**kw)
	else:
		weights = kw.get('weights')
		if weights is not None:
			kw['weights']=kw['weights'][ind]
		del kw['ind']
		idlplot.tvhist2d(a[ind],b[ind],*args,**kw)

def plothist(a,*args,**kw):
	ind = kw.get('ind')
	
	if ind is None:
		idlplot.plothist(a,*args,**kw)
	else:
		weights = kw.get('weights')
		if weights is not None:
			kw['weights']=kw['weights'][ind]
		del kw['ind']
		idlplot.plothist(a[ind],*args,**kw)

def plot(a, b=None, **kw):
	ind = kw.get('ind')
	
	if ind is None:
		idlplot.plot(a,b,**kw)
	else:
		del kw['ind']
		if b is not None:
			idlplot.plot(a[ind], b[ind], **kw)
		else:
			idlplot.plot(a[ind], None, **kw)
			

def oplot(a, b=None, **kw):
	ind = kw.get('ind')
	
	if ind is None:
		idlplot.oplot(a, b, **kw)
	else:
		del kw['ind']
		if b is not None:
			idlplot.oplot(a[ind], b[ind], **kw)
		else:
			idlplot.oplot(a[ind], **kw)


def ploterror(a,b,c,*args,**kw):
	ind = kw.get('ind')
	
	if ind is None:
		idlplot.ploterror(a,b,c,*args,**kw)
	else:
		del kw['ind']
		l = len(args)
		args1=[None]*l
		for i in range(l):
			args1[i]=args[i][ind]
		idlplot.ploterror(a[ind],b[ind],c[ind],*args1,**kw)
