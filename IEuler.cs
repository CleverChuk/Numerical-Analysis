/* IEuler.cs
*
*  Created on : May 7, 2017
* Author : CleverChuk
* Description:  
*   interface that defines the Euler class contract
*/
namespace Euler
{
    public delegate double fPointer(double t0, double y0);
    interface IEuler
    {        
        double[] solver(fPointer fptr, double t0, double y0, 
            double h, double t, int maxIter);
    }
}
