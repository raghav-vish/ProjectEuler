class pe1
{
	public static void main(String args[])
	{
		int s=0,i;
		for(i=1;i<1000;i++)
			if(i%3==0 || i%5==0)
				s+=i;
		System.out.print(s);
	}
}