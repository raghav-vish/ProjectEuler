class pe31
{
	public static void main(String args[])
	{
		long ways=8,v100,v50,v20,v10,v5,v2,v1;
		long startTime = System.nanoTime();
		for(v100=0;v100<200;v100+=100)
			for(v50=0;v50<200;v50+=50)
				for(v20=0;v20<200;v20+=20)
					for(v10=0;v10<200;v10+=10)
						for(v5=0;v5<200;v5+=5)
							for(v2=0;v2<200;v2+=2)
								for(v1=0;v1<200;v1++)
									if(v1+v2+v5+v10+v20+v50+v100==200)
										ways++;
		
		long duration = (System.nanoTime()-startTime);
		System.out.println(duration*1.0/1000000000);
		System.out.println(ways);
	}
}
