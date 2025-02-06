-- convert a databse to UTF-8

-- convert the database
ALTER DATABASE hbtn_0c_0
	CHARACTER SET utf8mb4
	COLLATE utf8mb4_unicode_ci;

-- use database
USE hbtn_0c_0;

-- convert first_table
ALTER TABLE first_table CONVERT TO
	CHARACTER SET utf8mb4
	COLLATE utf8mb4_unicode_ci;

