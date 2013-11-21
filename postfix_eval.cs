using System;
using System.Collections.Specialized;
using System.Collections.Generic;

namespace heap
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			Stack<int> s =new Stack<int>();
			string str= "532+8*+";
			char[] str_toChar=str.ToCharArray();
			 for(int i=0;i<str_toChar.Length;i++)
			{    
		
				int Num;
				bool isNum = int.TryParse(str_toChar[i].ToString(),out Num);
				if(isNum){
					s.Push(Num);
				}
				else{
					int num1=s.Pop();
					int num2=s.Pop ();
					switch(str_toChar[i].ToString ())
					{
					case "+":
						num1=num1+num2;
						break;
					case "*":
						num1=num1*num2;
						break;
					}
					s.Push(num1);
				}
			}
			
			System.Console.Write(s.Pop ());
		}
	}
}
