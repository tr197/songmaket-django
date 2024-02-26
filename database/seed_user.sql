INSERT INTO public."user" ("password",last_login,is_superuser,username,first_name,last_name,email,is_staff,is_active,date_joined,id) VALUES
	 ('pbkdf2_sha256$720000$z8Qsg6b7T1qgDdmR7R0p5U$dcQl2k2Enh5HzJNJ6SleJUtWnMG5ptGstvD1k9ckzGo=','2024-02-25 12:33:06.746841+07',true,'trinh','','','',true,true,'2024-02-25 12:32:48.263749+07','e408c282-f1ec-4bb6-ac5b-9873dac4a730'),
	 ('pbkdf2_sha256$720000$4Ofpop14G3F94j1arWc6Uc$wFzW5WT60HKcMrDlxwDm/uRqtaWfVnYZgl7+umS/p98=',NULL,false,'test1','','','test1@example.com',false,true,'2024-02-26 21:29:37.716044+07','1cd5ecda-da0b-4b5a-9907-7b2c5fb6733f'),
	 ('pbkdf2_sha256$720000$ne5W0QgkpCLV7cyuKEPKsp$8BAMOW7gepfRXQGvgX1LQWll39z+Bu6g0SqzLOXcmR8=','2024-02-26 21:44:59.615051+07',false,'test3','','','test3@gmail.com',false,true,'2024-02-26 21:44:59.108625+07','7f7ba453-e1f1-4847-b1d3-68ea4b41a243'),
	 ('pbkdf2_sha256$720000$IHi9H8l2qKTDZFPK3qwWRL$ue9UxbLV7yjJBPKjDhIcyDJAKdUm2z8D60+wjk3a3ZA=','2024-02-26 23:24:07.0292+07',false,'test2','','','test2@gmail.com',false,true,'2024-02-26 21:30:29.655668+07','83c03cfb-17ad-4fc5-97b0-2f04c442fd57'),
	 ('pbkdf2_sha256$720000$OcsQIzoVeYm0OkdnxnDmWV$lMMhu4va6ubYIguX61jReR+E5sSMZq26G57T/moYlPM=','2024-02-26 23:47:41.408429+07',false,'test5','','','test5@gmail.com',false,true,'2024-02-26 23:47:41.161182+07','a465885a-3e25-4101-a7bf-d8c2f9856732'),
	 ('pbkdf2_sha256$720000$c2NJn8m8Vim7pTmANhzFBt$NqCu+Tgwl/Zhbbi+qmEI+Ix8PD+LHzqcQJRY+uZcOmY=','2024-02-27 00:13:25.253255+07',false,'test4','','','test4@gmail.com',false,true,'2024-02-26 23:37:51.163259+07','6b93dcec-bd16-4ff1-961b-f68d08e7dae2');


INSERT INTO public.account_emailaddress (email,verified,"primary",user_id) VALUES
	 ('test1@example.com',false,true,'1cd5ecda-da0b-4b5a-9907-7b2c5fb6733f'),
	 ('test2@gmail.com',false,true,'83c03cfb-17ad-4fc5-97b0-2f04c442fd57'),
	 ('test3@gmail.com',false,true,'7f7ba453-e1f1-4847-b1d3-68ea4b41a243'),
	 ('test4@gmail.com',false,true,'6b93dcec-bd16-4ff1-961b-f68d08e7dae2'),
	 ('test5@gmail.com',false,true,'a465885a-3e25-4101-a7bf-d8c2f9856732');
