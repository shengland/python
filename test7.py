# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 10:59:33 2019
@author: Lee
"""
# 由getbooklist.py获得的所有书籍的名字和书籍的id清单，按次序形成列表，数据一一对应

bookid = ['9a4d5f16d036409abbf4758ff2629f20_4'];

# bookid = ['816ba20a-509c-42e2-ac4d-0fa570f3589d_4', '422fa33a-c407-4e82-81f5-b973ab3585fc_4',
#           '12ed19c5-1726-4834-99c6-8663533c4087_4', '88f461f5-0d5a-4bf5-b4e3-794ce287b780_4',
#           '6965a88b-f51c-492b-a7de-093f03f57e9c_4', '7fd056e748f0437594f7a08681364b77_4',
#           '55b11afb-2de9-401e-8292-bd19a2d2862a_4', '491c7d4b-e608-47c6-befd-b066bda26d89_4',
#           'e891ef19-77d5-4b3d-946f-cadefe39b616_4', '27ae7850-998d-4efe-8780-d99d397db195_4',
#           'bd1dd5cf-40f3-482c-9963-b87c6f31a51b_4', '105cf521-9fb4-473e-80a3-34e06f15f006_4',
#           '6ef32b6f-a2e2-424b-9f0b-d76102cb4e87_4', '76c092a8-2c13-4a2a-b29f-5879d803223c_4',
#           '7be2673efdd945b0a89307f3b539e39c_4', 'b592b8d1-e118-463f-b3b6-810c8856bfe0_4',
#           'a4cddcd5-46a7-447f-a871-8e7199b7bb9d_4', 'b6ec1a46-3ca5-40bb-be1e-7f94f5de193f_4',
#           '26ade51b-39b0-4ddf-a8fc-657f9f639dda_4', 'd79652c7-3b34-459e-b858-7a95fb349dda_4',
#           '6b9d7ea51c2a452c9094957a10744912_4', 'b525cd68-32a6-474d-b4e8-2549782a518e_4',
#           '1247aac36ac44b48ac522373a7a4c6b0_4', 'a4357cfb1da045b3be702b6faf85f9fb_4',
#           'df6e455e-ec93-4fc7-b98b-d7c13613220b_4', '4b9d8fe8-6a4c-4ba9-a7c6-2c01cc1e8e78_4',
#           '3a092ebd-28d0-4d00-bb8a-c70aa42435b1_4', '32f5fcc630e0473090304d14b4fe3039_4',
#           '5a29af5c03cf4e7e9c5427890e8067fa_4', '1621647c-25cb-4871-a242-29b2a21b9095_4',
#           '7c239366651a46399e5d67126a05c16a_4', 'd8be0fa5e5b747059b4d037fbb24de2c_4',
#           '9f8e1ea8-5fc9-44c7-a86d-0d433666e99f_4', '0b73ece2-5dda-4bc1-a340-4191e9e3d897_4',
#           '73b6edec-1def-4191-9f37-f9183f65ef28_4', '61a524d5-1829-4663-b2df-a93aa9792fc4_4',
#           'd165e58b-9aec-480e-ad15-89cccc50d6a4_4', 'e2cc32a9-6a4e-411e-bd98-e1f7f62e7731_4',
#           '1bfa9b12-f843-4a49-b64b-b65261bc4326_4', 'b9cc6127-817c-4304-b318-5235b9981c33_4',
#           '25da11b5e30d419cb2b0bdebe9213f3a_4', '2140ff8f-7ad6-4fda-aeb1-a52dbee31f5b_4',
#           '6a251b47-5708-4796-a962-a697ba9664d7_4', '4599c95b-79e1-4892-b22c-1003708a9396_4',
#           '1e669945-1d2e-4952-be3c-3424d8f1a32e_4', '248dfbab-feb5-403b-bc4d-5707dda7df90_4',
#           '51d1ac1d-072c-4d32-a24a-6087e2e7a455_4', 'ae0c85da-1476-43b0-9a62-ea0ad250bc92_4',
#           '8d5ac453-3d56-44ca-9421-10c7c33f1d93_4', '17c1905d-6517-4d53-a9c6-52d5a9c7b73b_4',
#           '7e6d7762-8e55-455b-92ef-ea0a1d018acd_4', '6e3522dc34674ec0b77e51819cde0869_4',
#           '0a7607801cac4ac19107ab7b518c273b_4', 'afdb7db0-8816-409c-b79d-44560a034e01_4',
#           '6efbf858-c39e-43aa-aea6-6255606542d0_4', 'c64ba567b9b54021b5f63fee7b7b0865_4',
#           '76a857d50f6d4bd28f3dbdb107ee0fdd_4', 'bf5830c9448643058c352d68d3c914b5_4',
#           '5bce1c3e-8c9a-4a90-b9bb-e87513470624_4', '38d1afee-48ce-4ce9-bdd1-81dba34516ef_4',
#           '081bfdc692b64630970b15d91a79f104_4', '7011ba54cb9c47d9a198697141d06731_4',
#           '65fdc05a-fcc4-4727-b88b-352863c82d7e_4', '1cadf456c8af4d89943a1b9b0c5eedd2_4',
#           '704d798d71af4d32a773ee20ad8f14e2_4', '0b288a3343c346c38cc4aefde7b39991_4',
#           '7ae2d69f-76c7-4bf2-981e-74f16f1b7350_4', '5005a9686e4e42769afb191505f760de_4',
#           'ccb8119dd87646d49752ed73f0ab672f_4', '9b9e17421ad14eb0ac3c7c1545d81ee1_4',
#           'd41dd623-4e2a-40f0-ac38-205be3e9ca87_4', 'a8190eee602144f19ba7d48acf261637_4',
#           'e2690a71a0574f46b5aaa9c8cb73be4f_4', '0df02e1e23cf4cffbda125f3e34d5c59_4',
#           'bacdb0ce-eccc-402a-8d77-097624928a11_4', '037b414c711a47a7abb2e37f5cd0a352_4',
#           '859594d5-2fa5-4e88-a1c4-588c0dec5b47_4', '3021bd8f-55c6-4ae9-8425-e1f6175dd713_4',
#           'a4ad75803bd449ffa771044b4cc78fbb_4', '2827464e-1cdf-4034-86c5-065f3dcfc7a5_4',
#           'c3944dc2dda14b02b26f43e201f591cd_4', '05485d8752d14ce49054ec103e5631b9_4',
#           '20ca6f01-77e7-429d-b08f-27a39c51a5a8_4', '9ffb0fe418be48f190c57432a909f719_4',
#           'eba5f99b2df44d1781d1e12e583d647c_4', '755efc52bfea49b5ba14a64ef78bc17f_4',
#           '4ea289dd-75eb-4a8b-8b56-5655806ab723_4', '7eb65a1123fe4884b5e3540f50c28d59_4',
#           'bc6e45d163b845068c465d30f8be57a5_4', 'c8bc5e92f3704bb6a3ec44927c355f20_4',
#           'a4270dba-a92d-4518-b53a-8852715538f4_4', '76b2c8fda9394673a7c9e36d94153443_4',
#           '2a00f83d4b1b4a76a5ccf902eedfe6c2_4', 'e64a8370cd494fb894381d5290cf8855_4',
#           '20dbcc47daf84e21b082f0917e617b9c_4', 'c46a8e0f-2f65-445a-a568-f2bfa36c2d32_4',
#           'd5152086-ea1b-4331-9b77-771e9af026b7_4', '3eedcecb-d829-402c-9e4d-941f6d9ab21f_4',
#           '7b4d0f76-dd9d-4886-a905-d9522a36ecfc_4', '40238c30cac54e92962e5ed4500846af_4',
#           'c9413a6e-20b3-43c3-b005-f464b941b849_4', '20e1ec56-4e90-49dc-b225-2f9131b1522c_4',
#           'f7001770a9d94bcebda4d5714307edf0_4', 'cc8fb282-ba1d-4fe9-b4f2-b4d6cda23b41_4',
#           '6ef856b8e61e4d11a123d13c43741ee0_4', 'b40708feb6f545b397986e50b4f25e4b_4',
#           '357136a54ea444a1b2a60206f2fb929b_4', '6fe3a5309de54acf9731949fbb5bebc6_4',
#           '8835893f-26a5-48cf-af9c-3714dfc76e34_4', '6eb8b8f1341848b1a250b4cd4262b806_4',
#           '10870ee730284ba89363d8cdfc8e3ae9_4', 'a8890424-dfb6-45d6-aa7c-4d9434ff1079_4',
#           '41da0a8486bb430980384b537563a117_4', 'afb8540f9dbe40678d2f6f912f9c756a_4',
#           'f031e7c6ffe9418a9538e111fa4612d4_4', '60f9d30138934117a6c0de56ae36c094_4',
#           '2646dec12617442fb68f1cc1eb4971f1_4', '8b62b68c-8d3e-4273-a78e-3dffaf3cb58a_4',
#           '429f3c1d2262492f94c0489a5591ac2c_4', '8da370132e944220baef8646448885e5_4',
#           'eb8f3de4b65e4c6792ae23dc701d0ec9_4', '5a96cb3fe91942daa1341d7da96e928e_4',
#           'c032b0a1cf284971b3974c2a7dc60d90_4', '8b868a94-28b0-4536-b465-14fd6ffb6c51_4',
#           '9a4d5f16d036409abbf4758ff2629f20_4', '11f6427d-4245-4c6f-9649-c98b429aa7cf_4',
#           '3fbbd7ef3d714727bc225dca17c8f0d5_4', 'df03beed988b4c01a6f58637ae992de7_4',
#           '668e3b9f919745c6928248bd9783be17_4', 'b2b9bf1a-5141-4cf1-b345-b5689bebb8f6_4',
#           '3402450595fa4cdb9293787abb811760_4', 'daa0336d2cfc4ef9b65beba7f1075868_4',
#           'dbd70b75e02440979ea0376793260853_4', 'faa76a40b11a4252a69cf5ac364faa35_4',
#           'c9ee68712eaa4f40a3eba11322d3cabf_4', '32762e96-6630-46d0-bf35-e6182d45f163_4',
#           '08087ecb-43fd-4668-b229-549d0b15d2ea_4', '7d98cd48304f4ba7a4cda62d90b482a2_4',
#           '3ed54fde-2420-4a3c-b724-bb2d4727bf80_4', 'a5247e0ebec84edd8664e838502c64a1_4',
#           'fe57ac999fcb4c6b9919d1aa360a8639_4', '20a214af-876e-4cd0-8277-0f4d3c5ec4b7_4',
#           'f4add9b525204f2d98c2884bdc0689b0_4', '290d7b5306b44d14bec6114841b88ea0_4',
#           '374fc8a0a9c44b2eb8c89c8bc8acc01e_4', '1a1b4db1a6104cd1b8811626c06412d4_4',
#           'b3cfef227c0e4b6488c50ef6129f32b2_4', 'eab751f60ee94181b171fbf8e83298e7_4',
#           'f4d1451f5b5449a492caaf406ff62aee_4', 'd10aaead33b84af6b0267c79b6fd3ba6_4',
#           'cb2e76484652452a8905faf4d9930b4d_4', '116744d3e31d4b93b0fb7d4997bbac00_4',
#           '956111d2240844408640d302b10b6ccf_4', '78a7b95363924bc1aec0c3784689b531_4',
#           'a1b3787f10bc4fea9f7e08707a4cfc07_4', 'f445114eb03a47a58ab405bd7aa0e8c1_4',
#           'edee79d87cc847cb8bad7012796791cc_4', '774195db79cc413faf4034bc5eaef4ae_4',
#           '1b130b506cc0477d964d7f18f3bc8659_4', 'fd16e28a37664c978b2a3fcfe74dd7bb_4',
#           '822a329e8d804fc7aee69328a32c7914_4', 'b28189c5dee14d0ab26d9f88f3c80ef2_4',
#           '516126cf419547eeb357bab4e78e4e9e_4', 'cb52c9e2e5f04e93977dd275b6398e5c_4',
#           'ce1f7ad759ad408ba3545654d042b1da_4', 'd03dc72d-781d-41c4-8dd5-13fc2377b189_4',
#           'dad71db6275c48d082a328a7d2193fcd_4', 'd979a3086ecc4e59bd44634c3cfcd122_4',
#           'ff15c605-76ee-4f1b-be68-5d6f2bd7ff08_4', 'e1d09b3a6bb745c38dd47d730fe9a4b2_4',
#           '6f90140843e14ef88c1307c400a9f1d5_4', 'cd81c097bb34488b8b6bd821192cca31_4',
#           '2768ac370943442db326b0c6a3cb6291_4', 'f02e01aed0f241c8b23d0c2e70ba4783_4',
#           'df608a807dc24d3986db55fff6220977_4', 'e98f62d06d214d7382795ac4a705af81_4',
#           '0789658e07cf407186fd56858b45a6b6_4', '00d32711d01d4a9888a3f673c44f2a2a_4',
#           '5d414d359fb849e2b80c578beec2bc23_4', '5582705dad144806892c5cecb8362cd4_4',
#           'c3f8e1a87d6d4518a9b79581a6bbc41d_4', 'a0c4b817-ce5e-445d-9fce-df69c986cba1_4',
#           '324416dfde9f4429895dc0ef49a702c1_4', '4c1c129f6b9a4e46937ff955007b2281_4',
#           'fd9dde17905448fcb0e544d928c3a56f_4', '09a85cd8ba9143479019a1651ffa2ae2_4',
#           '3ceb6c450d2d44a3a8701a1c83578db3_4', '125c70221b704c8596e588ed4cdaac06_4',
#           '904b86a9bd0a4a77a434c60ebff90e4d_4', '21d3b459f771479d947551aee915bedf_4',
#           '23e72fc0875742fd983a2f3d6e5fcf94_4', '0ad4bc0668554755b26300a13462ffc4_4',
#           'a8c8c39dcc654200ad03427f0798aee5_4', '928418a1-17ca-4813-813c-dbcba001f6c1_4',
#           '9cbe1ae57920431cbbfc3c1807d892fc_4', '93206b70cd7243738b0d7cb67e9ca707_4',
#           '1c7ca1c15d804b18aea5b74f1bdbf43d_4', 'd5064121b44b4ac2a9f31df2a19c753e_4',
#           'b673b377ff2745d88564f4678957bc80_4', '8cea4444affe424a856e7821b2b68f24_4',
#           'c2bf38b5424848e4b3e4aa875a28e670_4', '59f13d37-937f-43d7-a6c1-1e629066dd67_4',
#           '4bf1f5600bfc471f9d6449ff96075224_4', '256ab38a1d0449e2af4c8ca698e2e891_4',
#           '7aebffe87c094bdd8b48357fec0f72e8_4', '8166153fc02249d3b32d8fbd2f018475_4',
#           'a1227108c6504979af073d8d2f8c49d7_4', '81383aee5fc2485ca18bee2e4a4549b0_4',
#           '58a9d6dc1ec647c2a3b1c7e23f7671eb_4', '97df35bac79e4158805b93dc8206784b_4',
#           'ae26b9f5950744e1aa0d7e438b0b9634_4', '40a789c8408347c3afdfc593278f1de0_4',
#           'c46a233fbf194084b6849e877904ef89_4', 'bea3786fd58e42c59ab718e43537d762_4',
#           '0c6c76bc1f1840258e805e2b615b997b_4', '447054eb8b3243ea9041a62c09998cdc_4',
#           '58a57eeb072a45319f17fbee20c36f11_4', 'f49f624a0da74f098ff9008fd3636215_4',
#           '30a524e8e1584a4d9d50279636d58da5_4', '6977c89c14404cec855a238bedfcbbcd_4',
#           '1259bd7e12684c428a40c3979dc3fe02_4', '352cd3ac8f9d4ea796bf5fd014dc4ba2_4',
#           '33808109b5b849feaf7ea8f57e9adeaf_4', '12beb0270a864c2cbf56c03eed59e448_4',
#           '3049d75725af4384b419c5d0595e90ec_4', 'f458fb7b3ec842e6862fee089429c8eb_4',
#           'e5a4794770f040ecabf3190d167aed30_4', '26b409a78bb746c9a98aa5e6e2c53d5a_4',
#           '6e788b66178641509943edd2e82cf2a8_4', 'c53a187c77784e369d2c0afe3bc1e90f_4',
#           '1315f3a418c5449db79844b9fd885124_4', 'f69fe2ca990349dd8c4312d48c32686a_4',
#           'f020434912b748fcbbf245da520d514e_4', 'e934c1e19ac74cc5b1243acdd19d841b_4',
#           '27825964-4ec2-40be-aea7-394b167b5a3a_4', '52657ee5f886431f8e13a9800edd576f_4',
#           'aaea9321b2f14a4b993d4169332968da_4', '13da79ed-2b3a-4a20-a198-a213cef8b196_4',
#           'a77966856e6f494391b9ff4f6e18603f_4', '1c42a0e5b9be41eb95230f61729c51ed_4',
#           '63e6ed3d72004703b3ec53ff2abb5921_4', '8b371c1382ed49a88405872559ab75c1_4',
#           '8f8e6dd6f964426ca78ffff9c5ad5582_4', 'a49766a0641a4214ad39c3b135c095dc_4',
#           '493ab8373add45e09e4196a47b847901_4', 'b2f0e8462fef4911ba4c3f984e61b256_4',
#           '03dbd501677844a5a893f40b6b4f3287_4', 'ed9ad7c1cbe148428506383f9f54b349_4',
#           '5b0fd543f1dc47ae8b6307aa3da09e68_4', '739a7e5982204b13929385fa82d54349_4',
#           '5c38c42a4197461cbb52cc92944fd717_4', 'd7e9bf51079944c7ae6cce22f9494581_4',
#           '801104e2d99f48058a4e0cbbc9bd9b10_4', '127bc3ef2362483c8aab1a0d4cafda77_4',
#           'f2ea8fd564054f5e84d8b0ccf45e74c0_4', '38fdff1e681144419a075456e5080cc9_4',
#           '14db5e7d7b5f4d64bc1a6c8c0972aa69_4', '3c220cb2777e43719c5a413c6631be9b_4',
#           '4e4292730ad54729a159c491441f97a9_4', '46176fcf6d2e4aff9acd0e01af6a9dd4_4',
#           '536e77ec0f784afc9559fd23fbd546fe_4', 'ec1d41a633404e7e92c19b520bd70aac_4',
#           '9299fc99243e40229ac214059a83f581_4', '1ec6a5d0d2d4476885aad70f0413fc8b_4',
#           '8692a117cf9543a1a9677f0ff1b3a33a_4', 'a8f93a4f154a41d9814524262beb8af6_4',
#           '6bcf8ae5bb9e447780feb502538309dc_4', '1e223114c162427889fb14c808c886b5_4',
#           '031c19d7fdde4d0a95fb7276ea1def99_4', '953f702d2e7648e484831ca6be51d8c2_4',
#           '9ea026b150424b558bfbe11002990699_4', 'e93fa8c7b5d84cd5b95c20a0d7d3a3ee_4',
#           '0948aa9c580e4076836da8c605206f8e_4', 'ef11d46fcb4841669a5b035753ed1355_4',
#           '4305c06ef49f46d3a5a9fc928738b59f_4', '1616c67728eb4d3984ee07823f3361b1_4',
#           'ef6ec3a84265443ca60d99f235287cfe_4', '0169b32afe054331be9dd3ccaea913ce_4',
#           '482582fe-8185-475c-bc95-0f92d0329c3c_4', 'af7eb9136dba4f06acbcee3000e4b765_4',
#           '330ed38fa77345e8849badd8e3cdc8f3_4', 'a153103e001045d69b215d097d430a0e_4',
#           'ddf3349e-7aca-4394-901d-ee8414e42574_4', 'ca652969645f46e28281e1d98a660a57_4',
#           'ebcd4664ca9047d3a9764f0ec47c989e_4', 'ccc37208835b4dd7a96804bc9ba93715_4',
#           '613dbb80ce79431289e129bb8264a3b0_4', 'fa5a593e01b74903a191cbf7d44ec782_4',
#           '32d1be02fd7a4764b0a1bbfbae525f5a_4', '0016885b603d45539ec80a63bda24e66_4',
#           '02c5335ef6ff4ebe87144b43d2ba983c_4', '58eaa409b804411fa8870c052d8f8cf6_4',
#           '1f11bef3afba4885a4a36fe8a9fe2d94_4', '54f509723db84f3191a1daa40689b292_4',
#           '967d737f6a5c4cfd8ac3325f3e94a403_4', '7c8cd5ec036549feb008bf1088bf64b6_4',
#           '0e849f3daa5241e38f234b8c346e498e_4', 'eb0977465ef74fdf853d24a5dd281838_4',
#           '4ca8f580a2e344d39affa0caa45edf8d_4', '56518cbc185a41318f2dd8ba2bac6b40_4',
#           '0f6f5943f427473f86973306ce2fb15a_4', '0d016e5834f545d29aa3b6f540975296_4',
#           'a7484edd250e46f58df5308084b538f1_4', '86fbc9e9d38d42bca738a75091cd6307_4',
#           '7cfb1b72e6984c2ea7d7eb0507141c3c_4', 'aa47019c795440a6adf2c607c171a6a7_4',
#           '0a68bf8e2280427989f8b1b7d496c0d5_4', 'cbca6873231147ba875237a34f26dba7_4',
#           '77c34995d27148949cac64af0fde49c5_4', 'e93273efd6ce4b54834c97a47f886cbe_4',
#           '8d33781663184e9096e661cbdfef7619_4', 'bfa14b0fdd754bc4b72a4d7744ef60d2_4',
#           'd87813495006462396a339972cdf4646_4', '2ea10586f2504b5f9e071e61dab0e5b2_4',
#           '08329f2e9706405a8c6dfa2d31da98f9_4', 'e4f7cb0ff8234061ace5392a64d87cec_4',
#           '6b15a9d41a3a4762bff8c3b4cc5f7f72_4', '70a2e55e359d43cc9229a6f866362688_4',
#           '0152a65bee47485eaa57d6e9e4be65f3_4', '0c2d0b943e764e4bba00d91317b14522_4',
#           '8ebc3b357575477ea509b3467e60c627_4', '4e2eebc2500140cfaf4f24578a1766c0_4',
#           'b427e48491a94cf1b2c9c3a21f2261b3_4', 'f1b23cc61e1649408990f3892299844b_4',
#           '2acd984d14684d59a89c2e75acece445_4', '5f719e4c82ad467986ee92d01e5e3a78_4',
#           'cd79ab938bf040e482a1aa1c142a7c7a_4', 'e2b555b3-d6fe-4fd2-a783-e51990b5ad26_4',
#           '79d550eb7d93427ab0e53109f8f30312_4', '1236d981b4094ced81dbeb0a0f1ee7d1_4',
#           '7f26f73d8eb54ea49d27bcb73c4c51fb_4', 'f5a7c7d0dc0947088f0c411a9360a9f4_4',
#           'bb4717c04f3741709042e46993ebf413_4', '6eb960580b114d80813751734bae4b8c_4',
#           '5277ebaea1e9442e95794bb15ecd5c8a_4', '8616a248c54340a4b79740a2caa2fe72_4',
#           '92ae021cfb8f4ce9b5b73f179d594dfb_4', 'ace52632c3eb48cbbed33e19db7c661f_4',
#           '95dd818d840441b38f8cdb2ad2eb94c8_4', 'f73d92331de44f65b0ae7fd20a40adba_4',
#           '933c5449774845d8b51ee54741c17180_4', '814c51de3a8a48919047e80b9ca3b740_4',
#           'd41b01a3924e4156870365d022dd8b75_4', '187395de62ef4298a9692225cbd1e5c4_4',
#           'f685e9eb9029462eb7bb3ed0e36569ac_4', '4b05fb59b82845d8b25eedf8dfdcc974_4',
#           'e4860d67fd7e4bb08aa38125af40fd14_4', '6f8ada12e5b84b87b6d9df1cb1662881_4',
#           'd36723dfd5004121bfb317131b2ff849_4', 'c8d96e395a244efbaca11025543482d8_4',
#           '3bce4d4e1cef43a88b12d4d75c821795_4', '982914c05e204c4aaf9c4187093f088f_4',
#           '96c343a3fc264b608ac78e93a1df2c98_4', '4cb86cedf7034dc49dc2d5072cb3b869_4',
#           '97bd4d1ccdcf4637addd5e636026211e_4', '999e55ee63f54566a64f33d0abf23bf1_4',
#           '3c917b54-6c03-4d04-a1da-c3221495a10a_4', '506c5f0620d94a11aefae6dd3238837c_4',
#           'b01010a3016d40d38172f39e9cc7e29c_4', 'c71b845c7fa5487ca1e77d3218f2661f_4',
#           '90729dbd92394bc2974f275e7612bd6d_4', '0463c2da41804aa5ae19ab5aa3322a87_4',
#           '99044fd0de3a4735b997b832c430358e_4', 'a24ab5b20a5e46b0aad96a6812384416_4',
#           'fc6bc7ea84424ebeaa0912ce76a3de7e_4', '10e295376434488fbf8a4fdb33f0058e_4',
#           '44f6c3d5888e44c7b0f6497cfd622e53_4', 'b7373f3ebe3148129a6c7cfac909c79b_4',
#           '6cdb3b91f3b84899b6253de2e61409d5_4', 'acdda60fecf44da7bff111e85d2de079_4',
#           'a7cc7cf6237748b9878a43cdbbc5f905_4', '6d59d3941ff34e3e850866ba561e29ba_4',
#           '102a8f30bfa241eca3c82c1a24b41b94_4', 'ed8e1505d00d4b559dc7ce9619b1697e_4',
#           '7dc2e9d4959543dd9567437cc9238991_4', 'b33dca8ce96f427787056d2a27a12fa9_4',
#           'd03568ae775345c9887207183eb6609d_4', '02348ca4c7eb4cc9a29016595a8b505c_4',
#           '457962fb0843412e92d3db7ffc1f46e7_4', '90eb355c3f554f2ea27fcbd9c98b2d3b_4',
#           'b194b5e3110a4ab5811dd5469fa29893_4', '36795a4cf6c5434f9e4b9c752a9e1910_4',
#           '69d5f936d54e45f588e04556d6e3b9d8_4', '4bc1778a7ab74d65a4f698f508232f73_4',
#           'f0f37730e972464fa979247eddf4ade0_4', '6f8430f8c8b046a68ae356fa0e860744_4',
#           'c2867633398346c9991c1dbafff753c9_4', '8bec44d015a3424687c9396c1f76c708_4',
#           'a84ede1c05f4467489bef33130dba184_4', '715321fbdad545c08a9b693dee5fb55c_4',
#           '53f2b1b30c194fa2b5a2ce9447714f6f_4', '1c991411f78946e5878bb538b03c4a55_4',
#           '21267c26258048ebaee585edfbea917d_4', '8537fcf08b8e4492adcb1373cf25f095_4',
#           '437deb9a54d6458595a6fe932734b2d5_4', '2f22ea1da3ca4437b3f54f5470d9b83b_4',
#           'c27649dde8584dd2942c6833a8e75851_4', '59ed8b75ab0a4c738cd62cfead9e8795_4',
#           '88545244aa7a4461b2a5097491d1adf2_4', '196c462f28894378b51a85406c7365f0_4',
#           'fa2da9e976f94bd7a4c1e8f9c3250d47_4', 'da2d13b1b71f41b9ae4f287305ee78cb_4',
#           'bd9dd79de4ec4ea28c73498cdd4e2011_4', '77fe6d2652bd411085f5dbd0af815b42_4',
#           'c8e0057e2ae04f0a8dcd5ccd5b88b808_4', '26f2ee2304db41909991869a13382021_4',
#           '2549eecdcfc6468690236903fd3420c0_4', '74803dad514a4969a56ccc428f8442b8_4',
#           '7e9f567d011140e5b116c08d8dac90e0_4', '9b2dbb9eb1904777a820b0ad1a6b96b4_4',
#           '4c60372303fd4f5984193a8491abbcff_4', '5ad70851d7184b3ca5008a7ac810a376_4',
#           'cba87a3337284f7d97d063a452cc1382_4', 'e66a3976398f4447bcf48178b6eec79a_4',
#           'ebce2737d0ac424184281430c17d931d_4', 'ef8b21d1582042d7a6430a36682538b2_4',
#           'd44f23c46daf4893a5ee57b1038e3111_4', '92490922ebdf46b78948d3b3ab817dd6_4',
#           'f60954696c36496a9e0d6f093e6eef1b_4', '3af94961174049bba2ebabb71d1f5213_4',
#           '4899476b10bf43128542c89c84394535_4', '438a562d2cc8492a8189407db5a15801_4',
#           '2d61caebca654c31813c4d687e3c0afe_4', '27fb8757cfc7473596c2e83a091b9888_4',
#           '73f7e79aedde43f190150009a153b95b_4', '92c1b8d9cae149d6ba548828389296c2_4',
#           'fd9f7e30222d454390aeae0c1d44e5ed_4', '4cebe61c91ae46d39e2bf35ac4694c38_4',
#           '5cdf6fc2389c4df6a65605930c2aa1e5_4', 'a8dd052cd3534cfd94a31d5b242552f1_4',
#           '95570464e9c94775a97d1babf319a3b1_4', 'd208f1188e624ff08f6cb714fd31e1a8_4',
#           'e0f530298248426d80efd645770c3ebe_4', 'f5ff0919292c4078a842b8ad3afeebb9_4',
#           'a625a8fc0bc34ad5a736d9416377ab75_4', '23316d27647441b1bc6841e7a0ec05e4_4',
#           '6adc3bc0302343d0a92860c7ae7f228f_4', '10042644cb514828ae66ad3d7ad85ecd_4',
#           '92c02e9e2f9b4085a8c3a2fb3819bd24_4', 'aae8a8d8541845d1af612e050739f59b_4',
#           '100957bbc69747e1a1a0a850838ddc71_4', '1fd3d1c6168745f7b02c1491003ad783_4',
#           'd98e839ac61a490891088c7d4a45cd2a_4', 'b65fba3ae77049d7b7723b2c24a5f80d_4',
#           'ad892862d3ca42c3b9275a4892689409_4', 'ed9dfcd541b14b348d2c1e7156876522_4',
#           'a4b5e5ed46b44bc8afe14ed67b457972_4', 'cb5f0eac266e425ea6097038dd5610a6_4',
#           'ea558e6cfb7f47579e3a968fa38b4df4_4', 'd8d1eb4f59eb45c4bce2f48175eb25cd_4',
#           'f96f76bc639c460fb66a21eeba0efcaa_4', '17f522268a9741b4959aa417e302ed80_4',
#           '23c487e21d3e4a5d825bb3bccb29e41d_4', 'e0001e854e7447c59a05be3597d2e21c_4',
#           '515a06f5e5a641b7aef8568ccafb5ad5_4', 'df40c36151244c5781896aeaa4a46170_4',
#           '5fde5a35b5a14adc80a9c9a2e86f0d5e_4', '9d1df0807dcf4983866de943a2055b05_4',
#           'b1073be00e674b01b03b603093bf62aa_4', '3d7bb3daac5e4afbaac63455117d9387_4',
#           'b85f62ec92484c28b2d7aa041c77b9ef_4', '75cde3db31c240ceb058c4081c3dd705_4',
#           '114e6a3a73964ffba47e4f7e51b99f5f_4', '6cdd73929b294d74ba36e3ef87d56f23_4',
#           '8c5790dea48e4a18a4ffcd1d11361e85_4', '4df76a79a82c4ea4a75633453838efdd_4',
#           'c8e8b2e688ef4731af1fd5b6e4145fc7_4', '4f06cdab052d4c3abe783fc9ec463054_4',
#           'cf65d055034d49a486e4f57bead1bb87_4', '838491aab5c14879b68e171b4ba7c50c_4',
#           '433446b2375e4eed9f63f32f77d0090b_4', 'cfbcc22a14ce49e3aa0b0832c126c226_4',
#           '770ffa57b312445589b3dc32e2bf542e_4', 'd8999ad474ae4cf6adfa9f50eb6b865e_4',
#           '130d3a7978af456483347f2d6395916e_4', '060298192104454e868593ba7fc7675b_4',
#           '62d5ea228ff8462a81b47fef82d26b2f_4', '9503f582f17d4b959f16c6e7067b1799_4',
#           '7cbdc3367d9f410a8bd022314703152f_4', '2820abd0b3aa405899b53f01449bf1d0_4',
#           '0efa4d0aab644846a515eb369308977e_4', 'fc891911bc384eac8254a7832e6d6935_4',
#           '8e8b090a207d48068956a667b9d83ac7_4', 'aad4bed3c53b4d0bbafe36f9a53888a6_4',
#           '81264b1eb5984872877332211f2c8318_4', '7f11e71c357b430c9449feb371e8049a_4',
#           'f3405bd79720438d92cbc5819b8d1f9c_4', 'c9440ed362d145dda4f3bc10f31bac96_4',
#           '54df300bd2c24b389f76a8a0acc459b5_4', 'afd10b77ffdc4112a04cec9c1ad5fef7_4',
#           'ad104f0f4d114da8b7509d7d3e14d07b_4', 'd60c439eb90640d08dfa4477b4dcd712_4',
#           'c543372e082d47ba81bda60fb298f2a4_4', '7645bc80b5374bc8b915c88f5cd9e2aa_4',
#           '52c6bbb7ad3f46ba81c2157284332736_4', 'd11dc8137ffa40ebb06670c4b35c0d76_4',
#           '514d511b262549f18d69dcca9b585335_4', '105eaa8fbdfd4beb8b6e589cc8535928_4',
#           '9a9225df6e264a0194ad6e9370fe2c27_4', 'c44357833e784e0b9ade347b8c2139ee_4',
#           '2fcf8a286c2a47c0b766753fedcfc2f0_4', '2e000a6bdd7941aba7bc58ec872d55ed_4',
#           'c203a74ef6ce4297ad58347dfff2d5e9_4', '3239fb7c7bbe41babc9a6f432275d871_4',
#           '95815cfce4264dbda0a74457f9b0f745_4', '9f6fc5ca3eca41cbac78074d42823c96_4',
#           'eba69b3e809c4a5086501154e9c5bd4d_4', 'fe841078cd3f487aa2c3d9e4a3f32b1c_4',
#           'bd13ff102dd94bcfb0a0a5bbbbdd603f_4', '3549ae4539204ac699455e3912023f95_4',
#           'a35ad76532124fe9991f60d909a8bf21_4', '554e2f699e6845b7a792366003ee1272_4',
#           'fee67b1b67734a18a7b0020a810d7a0a_4', 'd36152d54d234235aa39012e37e360df_4',
#           '7ff53391565f47aebbd442fdae679239_4', 'da9c056119a845b5b941e1121389837f_4',
#           '0f313ee70c3c43f5a1b7ab320fc3c2d5_4', '6ea5e0f400c1450ab1cf26a7e73eeac7_4',
#           'f8ed266caeb64629857980c25e41d40f_4', 'e76bbbdf79ec46c191fd6113ea7da158_4']
# name = ['三国演义', '红楼梦', '水浒传', '儒林外史', '西游记', '浮生若梦', '浮生六记', '牡丹亭', '西厢记', '文心雕龙', '镜花缘', '警世通言', '封神演义', '醒世恒言',
#         '金瓶梅（上册）', '汉赋选', '东周列国志', '隋唐演义', '孽海花', '西游记补', '金瓶梅（下册）', '二刻拍案惊奇', '红牡丹', '管锥编1（节选）', '狄公案', '隔帘花影', '锋剑春秋',
#         '金瓶梅', '红楼梦', '花月痕', '滴天髓', '红楼梦（上册）', '柳宗元集', '醉醒石', '窦娥冤', '残唐五代史演义传', '杜工部集', '杨家将', '观音菩萨传奇', '东游记',
#         '红楼梦（下册）', '钟馗斩鬼传', '玉蟾记', '归莲梦', '章台柳', '儿女英雄传', '三遂平妖传', '水石缘', '商界现形记', '泪珠缘', '双和欢', '水浒传', '西游记', '醉古堂剑扫',
#         '白话搜神记', '玉楼春', '北史', '神异经', '杨乃武与小白菜', '毛公案', '姑妄言', '中华好诗词：第2期题库', '四大美人艳史演义', '紫钗记', '三国演义', '脂砚斋全评石头记',
#         '后三国演义', '三续金瓶梅', '三国志', '菜根谭', '歌德谈话录', '怡情阵', '中华好诗词：第9期题库', '醒世姻缘传', '三刻拍案惊奇', '大宋宣和遗事', '笏山记', '恨海', '春秋繁露',
#         '薛刚反唐', '山海经', '中华好诗词：第17期题库', '后西游记', '仇池笔记', '东京梦华录', '中华好诗词：第12期题库', '玄怪录', '地藏经', '六祖坛经', '黄庭经', '小五虎演义',
#         '红楼春梦', '左传', '中华好诗词：第16期题库', '华严经', '说苑', '五大奇书', '倩女离魂', '荡寇志', '洞冥记', '拾遗记', '续西游记', '三国演义（上册）', '剪灯余话',
#         '薛丁山征西', '古文观止', '初刻拍案惊奇', '周易', '皮五辣子', '酉阳杂俎', '石头记索隐', '南柯太守传', '飞花艳想', '易传', '三国演义（下册）', '儒林外史', '浮生六记',
#         '岂有此理', '续金瓶梅', '醋葫芦', '九尾龟', '官场现形记', '三国志平话', '十尾龟', '李白全集', '夜谭随录', '度心术', '阅微草堂笔记', '苏轼全集', '绣屏缘', '文选',
#         '世说新语', '古文辞类纂', '文心雕龙', '再生缘', '稽神录', '金台全传', '风筝误', '异苑', '聊斋志异', '隋唐演义', '娇红记', '古本水浒传后50回', '艺术典术数部汇考奇门遁甲',
#         '水浒传（上册）', '楞伽经', '香艳丛书', '水浒古本', '范子计然', '警世通言', '锦绣衣', '圆觉经', '东坡乐府', '古本竹书纪年辑证', '西游记百回详注', '水浒传（下册）',
#         '明史演义', '东周列国志', '水浒新传', '古小说钩沉', '汉书', '封神演义', '安士全书', '初刻拍案惊奇', '醒世恒言', '右台仙馆笔记', '南游记', '水浒后传', '北梦琐言',
#         '王阳明靖乱录', '二刻拍案惊奇', '蔡东藩前汉演义', '抱朴子内篇', '文苑英华', '唐传奇选辑', '续资治通鉴', '蔡东藩宋史演义', '蔡东藩唐史演义', '博物志', '洛阳伽蓝记', '两晋演义',
#         '鸳鸯配', '昭明文选', '古列女传', '经史百家杂钞', '说唐', '楚辞', '《薛刚反唐》全集', '怡情佚史', '蔡东藩五代史演义', '银瓶梅', '西游补', '清朝三百年艳史演义', '觅灯因话',
#         '陶渊明全集', '武则天外史', '蔡东藩清史演义', '全上古三代秦汉三国六朝文', '续三国演义', '玄要篇', '蔡东藩元史演义', '尧山堂外纪', '风月鉴', '酉阳杂俎', '清朝秘史',
#         '贵妃艳史演义', '博物志', '隋唐野史', '封神演义', '金屋梦', '红楼梦补', '西游记（上）', '南北史演义', '李义山诗集', '李太白文集', '列异传', '智囊全集', '南北史演义',
#         '七侠五义', '说唐后传', '西太后艳史演义', '风月梦', '酌中志', '后山诗话', '儒林外史', '武则天四大奇案', '板桥杂记', '唐代宫廷艳史', '杜甫全集', '石点头', '夜雨秋灯录',
#         '后红楼梦', '红楼梦影', '西游记（下）', '中国通俗说唱作品集—富贵神仙', '东西汉演义', '容斋随笔', '新民公案', '饮冰室评词', '歧路灯', '玉娇梨', '梦溪笔谈', '柳如是集',
#         '上古秘史', '后西游记 ', '大慈恩寺三藏法师传', '唐宋八大家文钞', '列仙传', '辨症玉函', '桃花扇', '墙头马上', '文昌孝经', '元曲三百首', '陆游全集', '窥词管见', '清风闸',
#         '古代英烈传续', '后水浒传', '西游真诠', '金莲仙史', '东游记', '说唐全传', '陆九渊集', '西厢记', '隋唐演义', '好逑传', '小五义', '玉簪记', '问花楼词话', '睡虎地秦墓竹简',
#         '怀麓堂诗话', '济公全传', '陆放翁全集剑南诗稿渭南文集', '国语', '苏轼集', '三侠剑', '五杂俎', '韩愈全集', '鉴诫录', '西游记传', '清宫十三朝演义', '粉妆楼全传',
#         '中国通俗说唱作品集—禳妒咒', '四游记', '残唐五代史演义传', '续红楼梦', '续红楼梦未竟稿二十回', '醒世姻缘传', '残水浒', '存家诗稿', '狄青演义', '反唐演义全传', '帝鉴图说',
#         '五美缘全传', '续红楼梦新编', '辰州符咒大全', '雍正剑侠图', '貂禅艳史演义', '陈氏香谱', '鼓掌绝尘', '补红楼梦', '续西游记 ', '古文小品咀华', '五虎平西', '青楼梦 ',
#         '新西游记', '痴人福', '冲虚经', '醒世姻缘传', '幽梦续影', '八洞天', '女仙外史', '谷音', '夏商野史', '欧阳修全集', '永庆升平前传', '新石头记', '喻世明言', '永庆升平后传',
#         '唐祝文周四杰传', '汉赋', '镜花缘', '开辟演义', '八仙得道', '醒世恒言', '柳宗元全集', '西施艳史演义', '中国通俗说唱作品集—墙头记', '志怪录', '东渡记', '连城璧外编',
#         '花间集', '寒山子诗集', '东坡全集', '西游补', '绿野仙踪', '昭君艳史演义', '水浒传注略', '雷峰塔奇传', '萤窗异草', '魏阉全传', '警世通言', '古文观止', '廿载繁华梦',
#         '续水浒传', '雨花香', '十二笑', '说唐三传', '无声戏', '万花楼', '集异记', '后官场现形记', '包公案', '红楼复梦', '五虎平南', '花月痕', '中国通俗说唱作品集—蓬莱宴',
#         '清平山堂话本', '野叟曝言', '长春真人西游记', '续济公传', '石头记索隐', '女聊斋志异', '今古奇观', '汉武故事', '二刻醒世恒言', '六朝文絜', '争春园', '观音菩萨传奇',
#         '红楼余梦', '双凤奇缘', '长安志', '续镜花缘', '说岳全传', '东西汉演义', '照世杯', '乡曲枝辞', '合浦珠', '聚仙亭', '草木传草木春秋药绘图', '蝴蝶缘', '艺舟双楫', '琵琶记',
#         '词综', '夏完淳诗词曲赋', '五虎平南', '韩湘子全传', '孽海花', '盘古至唐虞传', '志怪', '英烈传', '桃花女阴阳斗传', '七剑十三侠', '集千家注杜工部诗集', '小儿头面耳目鼻病门',
#         '龙凤再生缘', '东西晋演义', '锦香亭', '戏蛾记', '新编五代史平话', '救风尘', '晚清文选', '飞花咏', '新水浒', '青红帮演义', '红楼幻梦', '绣鞋记', '甄异传', '说唐后传',
#         '薛仁贵征东', '飞跎全传', '林泉高致集', '李文忠公选集', '草阁诗集草阁文集筠谷诗集', '小五义', '彭公案', '琅嬛记', '朝野佥载', '小豆棚', '吴三桂演义', '儿女英雄传',
#         '武王伐纣平话', '老残游记', '草木子', '鹿樵纪闻', '燕子笺', '说岳全传', '唐钟馗全传', '花月尺牍', '婆罗岸全传', '淞隐漫录', '醉翁谈录', '古诗源', '百川书志', '白石诗集',
#         '萨真人得道咒枣记', '双灯记', '窦娥冤', '唐代墓志汇编续集', '续英烈传', '歇浦潮', '后宋慈云走国全传', '麟儿报', '泣红亭', '西夏书事', '长生殿', '柳宗元集', '玉蟾记',
#         '唐三藏西游厄释传', '隋史遗文', '西湖二集', '怪病门', '妇人产后门', '唐书志传通俗演义', '吴江雪', '录异传', '轰天雷', '小五虎演义', '妇人临产门', '博异志', '历代词话',
#         '万锦情林', '玉燕姻缘全传', '通天乐 ', '绿牡丹', '引凤萧', '斩鬼传', '乐府阳春白雪', '悬笥琐探', '大汉三合明珠宝剑全传', '刘生觅莲记', '绘芳录', '混唐后传', '市声',
#         '白云集（元释英）', '善恶图全传', '简斋诗集', '莲子居词话', '七十二朝人物演义', '寒门', '蕙风词话', '彭公案', '咏物诗', '鬼谷四友志', '东坡诗集', '英云梦传', '文明小史',
#         '屈原全集', '汉宫秋', '永庆升平前传', '全蜀艺文志', '终须梦 ', '英烈传', '发财秘诀', '两晋秘史', '杨家将', '说呼全传', '白云仙人灵草歌', '白雨斋词话', '杭州志',
#         '东山存稿', '顾亭林诗文集', '续侠义传', '铁围山丛谈', '菽园杂记\u3000', '续济公传', '金台全传', '仙卜奇缘', '鼓琴训论', '醒风流', '岭南逸史', '胡涂世界', '八贤传',
#         '东坡乌台诗案', '贵耳集', '刘公案', '玉台新咏', '庚子国变记-清-罗惇曧', '赛红丝', '五虎平西演义']
name = ['李白全集']

import requests
import base64
from bs4 import BeautifulSoup
import random
import time
import numpy as np
import re
import os

url = 'http://yuedu.163.com/getBook.do?id={}&tradeId='
user_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    # iPhone 6：
    "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",
]

headers = {'User-Agent': random.choice(user_agent),  # 随机选取头部代理
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
           'Connection': 'keep-alive',
           'Cookie': '_ntes_nnid=933c525f8c0b999244d85429df9c54ed,1560650274521; _ntes_nuid=933c525f8c0b999244d85429df9c54ed; mail_psc_fingerprint=4c89f9e89b2b7fe2b11bf2c401bfd48d; P_INFO=lyc4481341234@163.com|1561010733|0|mail163|00&99|null&null&null#anh&340100#10#0#0|&0|urs&unireg|lyc4481341234@163.com; YUEDU_V_DID=1561101191676127; __utmz=63080999.1561101194.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); davisit=1; __da_ntes_utmz=63080999.1561101210.1.1.utmcsr%3D(direct)%7Cutmccn%3D(direct)%7Cutmcmd%3D(none); __da_ntes_utmfc=utmcsr%3D(direct)%7Cutmccn%3D(direct)%7Cutmcmd%3D(none); Province=0; City=0; YUEDUDYAMIC=73b63802c56bb10183fabdbf5f94b10d5c3f562e; __utmc=63080999; NTESYUEDUSI=7061C64B294D0A5BEEC4591C452033B5.hzabj-yaolu54.server.163.org-8010; __utma=63080999.1028985031.1561101194.1561344730.1561355102.4; __da_ntes_utma=63080999.209114706.1561101210.1561345962.1561355217.5; __utmb=63080999.28.7.1561355537272; __da_ntes_utmb=63080999.3.10.1561355217'
           }

# 页面解析 两种方式 一种用BeautifulSoup，另外一种用正则解析
'''
def parsehtml(html):
    text=[]
    soup=BeautifulSoup(html,'html.parser')
    try:
        t=soup.find(attrs={'class':'m-content'})
        if t.find('h1'):
            text.append(t.find('h1').text)
        for i in t.findAll('p'):
            text.append(i.text)
    #print(text)
        return "\n".join(text)
    except:
        return "Error"
'''


def parsehtml(html):
    c = re.split("<.*?>", html)
    cc = filter(lambda x: len(x) > 3, c)
    return "\n".join(cc)


def save_to_txt(items, bookname):
    with open('{}.txt'.format(bookname), 'a', encoding='utf-8') as f:
        f.write('#@#' + '\n')
        f.write(str(items) + '\n')
def review_page(each_url):
    b = requests.get(each_url, headers=headers).json()
    content = base64.b64decode(b.get("content")).decode()
    onecontent = parsehtml(content)

    print('\033[0;33m爆竹声中一岁除，')
    print('春风送暖入屠苏。')
    print('千门万户曈曈日，')

    print(each_url)
    print('*' * 24)
    print('#@#' + '\n')

    print(str(onecontent) + '\n')
    print('\033[0m')

def main():
    each_url = 'http://yuedu.163.com/getArticleContent.do?sourceUuid=8355808f10e0459fbe97d5a4b88a83bd_4&articleUuid=671110c69d3d485686194174e78f7605_5&bigContentId=8796093024380498249&t=1574820197585'
    review_page(each_url)

def main1():
    count = 0
    for idx in bookid:
        a = requests.get(url.format(idx), headers=headers, timeout=30).json()
        list1 = a.get("portions")
        uuid = []
        contentid = []
        for i in list1:
            uuid.append(i['id'])
            contentid.append(i['bigContentId'])

        for i in range(len(uuid)):
            print('\033[0;36m爆竹声中一岁除，')
            print('春风送暖入屠苏。')
            print('千门万户曈曈日，')
            print('总把新桃换旧符。\033[0m')
            each_url = 'http://yuedu.163.com/getArticleContent.do?sourceUuid={}&articleUuid='.format(idx) + \
                       uuid[i] + '&bigContentId=' + contentid[i]
            b = requests.get(each_url, headers=headers).json()
            content = base64.b64decode(b.get("content")).decode()
            onecontent = parsehtml(content)
            print(each_url)
            print('*'*24)
            print('#@#' + '\n')
            print('\033[1;33;41m')
            print(str(onecontent) + '\n')
            print('\033[0m')


                    # save_to_txt(onecontent,name[count])
        print("已经下载完第{}本书".format(count))
    # 加上随机的时间延迟
    rdtime = 50 * np.random.rand()
    time.sleep(rdtime)


if __name__ == "__main__":
    main()