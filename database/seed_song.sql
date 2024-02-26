INSERT INTO public.banner (id,image,title) VALUES
	 ('abbf01bc-a41e-4601-8660-63b43665c01e','images/banners/b1.png','dj'),
	 ('f67449cb-30b1-470f-98fd-7512d07a1afe','images/banners/b2.png','drum'),
	 ('9647ab53-39b9-4aa2-95cf-63a1b86c4558','images/banners/b3.png','piano');


INSERT INTO public.song_artist (id,"name") VALUES
	 ('3d83a589-5aca-4f6e-b37c-6aaf1118035f','BABYMONSTER'),
	 ('1d6f3e34-ddb6-448b-b9c6-a96eb773c0e8','Maroon 5'),
	 ('7c8ee915-e3fc-4e6b-8aaa-dd1e03169235','NewJeans'),
	 ('18f50687-a45d-4f0f-919e-8338b3d8a318','LE SSERAFIM');


INSERT INTO public.song (id,title,audio,album_id,artist_id,image,created_at,updated_at,view_count) VALUES
	 ('3537ee4d-8b50-401d-b6e1-21f1bbbcc84a','UNFORGIVEN','songs/audio/LE_SSERAFIM_UNFORGIVEN_feat._Nile_Rodgers_4K_128_kbps.mp3',NULL,'18f50687-a45d-4f0f-919e-8338b3d8a318','songs/image/unfoginven.jpg','2024-02-26 12:37:50.306436+07','2024-02-26 15:15:45.617873+07',1),
	 ('6d33b24b-5c1f-4322-aed7-152361904b41','Smart','songs/audio/Smart__LE_SSERAFIM_COMEBACK_SHOWCASE_EASY_128_kbps.mp3',NULL,'18f50687-a45d-4f0f-919e-8338b3d8a318','songs/image/easy.webp','2024-02-26 12:49:12.232344+07','2024-02-26 15:18:49.643308+07',4),
	 ('bd8dc1f0-982c-4a17-9000-7beba1db2404','Perfect Night','songs/audio/Perfect_Night.mp3',NULL,'18f50687-a45d-4f0f-919e-8338b3d8a318','songs/image/Perfect_Night.jpg','2024-02-26 12:42:09.566705+07','2024-02-26 15:18:58.066123+07',1),
	 ('fd6d9240-db01-4890-bed5-7ee55e9faed5','GODS','songs/audio/NewJeans_-_GODS-320_kbps.mp3',NULL,'7c8ee915-e3fc-4e6b-8aaa-dd1e03169235','songs/image/GODS.webp','2024-02-25 17:03:44.792224+07','2024-02-26 17:54:19.457075+07',2),
	 ('d9f8ca83-767d-4984-8538-edf184dbdb1f','Stuck In The Middle','songs/audio/Stuck_In_The_Middle_M_V_320_kbps.mp3',NULL,'3d83a589-5aca-4f6e-b37c-6aaf1118035f','songs/image/Stuck_in_the_Middle.png','2024-02-25 16:38:10.359689+07','2024-02-26 11:24:14.157666+07',3),
	 ('8b280143-a246-4524-acc9-d14966a7d7e7','BATTER UP','songs/audio/BABYMONSTER_-_BATTER_UP_M_V_320_kbps.mp3',NULL,'3d83a589-5aca-4f6e-b37c-6aaf1118035f','songs/image/batter-up.jpg','2024-02-25 16:33:59.352625+07','2024-02-27 00:13:35.757363+07',9),
	 ('c7e6a911-58e8-4b2a-a081-83f689e741db','New Jeans','songs/audio/New_Jeans-NewJeans_Choreography-320_kbps.mp3',NULL,'7c8ee915-e3fc-4e6b-8aaa-dd1e03169235','songs/image/newjean-newjean.jpg','2024-02-25 16:54:45.221686+07','2024-02-26 11:34:03.657427+07',3),
	 ('5e6bf1a8-5920-4006-b109-bcca3dc8b27a','ETA','songs/audio/NewJeans_뉴진스_ETA_Official_MV_320_kbps.mp3',NULL,'7c8ee915-e3fc-4e6b-8aaa-dd1e03169235','songs/image/newjean-newjean_9e4PKoG.jpg','2024-02-25 16:58:58.732221+07','2024-02-26 11:35:19.538545+07',2),
	 ('f4a35055-d5d5-42d3-b526-27495e93c1ac','One more night','songs/audio/Maroon_5_-_One_More_Night.mp3',NULL,'1d6f3e34-ddb6-448b-b9c6-a96eb773c0e8','songs/image/one-more-night.jpg','2024-02-25 16:41:47.046542+07','2024-02-26 12:27:16.806454+07',0),
	 ('d0662dff-a331-4c24-baaa-2cb31c9bda1e','Beautiful Mistakes ft. Megan Thee Stallion','songs/audio/Maroon_5_Beautiful_Mistakes_Lyrics_128_kbps.mp3',NULL,'1d6f3e34-ddb6-448b-b9c6-a96eb773c0e8','songs/image/Maroon_5_and_Megan_Thee_Stallion_-_Beautiful_Mistakes.png','2024-02-25 16:47:44.491881+07','2024-02-26 12:28:43.125603+07',1);
INSERT INTO public.song (id,title,audio,album_id,artist_id,image,created_at,updated_at,view_count) VALUES
	 ('fedaea71-d918-406d-9e8b-fb6169a0b778','Zero','songs/audio/NewJeans_Zero_Performance_Video_128_kbps.mp3',NULL,'7c8ee915-e3fc-4e6b-8aaa-dd1e03169235','songs/image/newjean-zero.jpg','2024-02-26 12:32:17.359003+07','2024-02-26 12:33:13.876762+07',2),
	 ('f72c9c7b-217d-4ab1-94b3-df4021d2c690','This Love','songs/audio/Maroon_5_-_This_Love_Lyrics_128_kbps.mp3',NULL,'1d6f3e34-ddb6-448b-b9c6-a96eb773c0e8','songs/image/this-love.jpg','2024-02-25 16:50:41.447731+07','2024-02-26 12:38:14.364459+07',1),
	 ('6dbaab5b-103c-4749-9e68-fdcc560e112c','Flash Forward','songs/audio/Flash_Forward_LE_SSERAFIM.mp3',NULL,'18f50687-a45d-4f0f-919e-8338b3d8a318','songs/image/unfoginven_dxCw9o3.jpg','2024-02-26 12:46:44.005358+07','2024-02-26 12:46:44.005358+07',0);
