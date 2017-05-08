/* Euler.cs
*
*  Created on : May 7, 2017
* Author : CleverChuk
* Description:
*   Implementation of Euler's Method for first ODEs
*/
using System;
namespace Euler
{
    public class Euler : IEuler
    {
        public double TOL { get; set; } = 1e-4;

        public double[] solver(fPointer fptr, double t0, double y0, 
            double h, double t, int maxIter)
        {
            double[] yvalues = new double[maxIter];
            yvalues[0] = y0;

            for (int i = 1; i < maxIter; i++)
            {
                yvalues[i] = (yvalues[i - 1] + h * fptr(t0, yvalues[i - 1]));
                t0 += h;

                if(Math.Abs(t0-t)< TOL)
                {
                    break;
                }
            }
            return yvalues;
        }
    }
}
