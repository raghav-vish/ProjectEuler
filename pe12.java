class pe12
{
	static long nof(long n)
	{
		long f=0;
		for(long i=1;i<n/2;i++)
		{
			if(n%i==0)
				f+=2;
			if(i*1.0==n*1.0/i)
				f--;
		}
		return f;
	}

	public static void main(String args[])
	{
		long nf,i=1,tri=0;
		while(true)
		{
			tri+=i++;
			if(nof(tri)>500)
				break;
		}
		System.out.print(tri);
	}
}