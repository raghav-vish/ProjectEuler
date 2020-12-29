class pe9
{
	public static void main(String args[])
	{
		int a,b,c;
		outer:
		for(a=1;a<1000;a++)
			for(b=1;b<1000;b++)
			{
				c=1000-a-b;
				if(a+b>c && b+c>a && a+c>b && c>b && a*a+b*b==c*c)
				{
					System.out.print(a*b*c);
					break outer;
				}
			}
	}
}