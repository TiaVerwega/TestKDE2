from scipy import stats

def function(data):
    result = stats.gaussian_kde(data)
    
    return result
    
