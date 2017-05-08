/* Program.cs
*
*  Created on : May 7, 2017
* Author : CleverChuk
* Descriptions:
*   This program test drives the implementation of Euler's Method
*/
using System;

namespace EulerDriver
{
    public delegate double mydel(double d1, double d2);
    class Program
    {
        static void Main(string[] args)
        {
            Euler.Euler solver = new Euler.Euler();
            mydel del = func;
            double t0 = 0;
            double y0 = 1;
            double h = 0.001;
            double t = 5;
            int maxIter = 10000;

            double[] soln = solver.solver(func, t0, y0, h, t, maxIter);

            foreach(var item in soln)
            {
                if (item == 0)
                    break;
                Console.WriteLine(item);                
            }
            Console.ReadKey();
        }
        private static double func(double t0, double y0)
        {
            return (2-Math.Pow(Math.E, -4*t0)-2*y0);
        }
    }
}
