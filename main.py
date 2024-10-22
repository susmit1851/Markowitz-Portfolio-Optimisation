from utils import *

num_securities=10
returns=pd.read_csv('Data.csv')
returns=returns[[f'col_{i}' for i in range(10)]]

sigma=np.array(returns.cov())
mu=np.array(returns.mean())

gamma=0.020
G=np.linalg.cholesky(sigma)

with mf.Model('Markowitz_Optimisation') as M:
    x = M.variable("x", num_securities, mf.Domain.greaterThan(0.0))
    M.constraint('budget', mf.Expr.sum(x), mf.Domain.equalsTo(1.0))
    M.objective('obj', mf.ObjectiveSense.Maximize, mf.Expr.dot(mu, x))
    M.constraint('risk', mf.Expr.vstack(gamma, 0.5, mf.Expr.mul(G.T, x)),
                    mf.Domain.inRotatedQCone())
    M.solve()
    expected_return=M.primalObjValue()
    portfolio=x.level()
    print("Optimal Portfolio Allocation:", portfolio)
    print("Expected Portfolio Return:", expected_return)