CREATE DATABASE QLSVPY
go
USE QLSVPY 
GO 

CREATE TABLE ACCOUNT(
	MaAC varchar(10) PRIMARY KEY,
	username varchar(20),
	pass varchar(20),	
	roles varchar(20)
)

CREATE TABLE SINHVIEN(
	MaSV varchar(10) PRIMARY KEY,
	TEN varchar(255),
	Gioitinh varchar(20),
	Ngaysinh smalldatetime,
	Sdt varchar(255),
	Email varchar(255)
)

CREATE TABLE GIANGVIEN(
	MaGV varchar(10) PRIMARY KEY,
	TenGV varchar(255),
	Gioitinh varchar(20),
	Sdt varchar(255),
	Email varchar(255),
	MaAC varchar(10) REFERENCES ACCOUNT
)

CREATE TABLE MON(
	MaMon varchar(10) PRIMARY KEY,
	TenMon varchar(255),
	MaGV varchar(10) REFERENCES GIANGVIEN
)

CREATE TABLE DIEM(
	MaSV varchar(10) REFERENCES SINHVIEN,
	MaMon varchar(10) REFERENCES MON,
	Diem decimal(3,1)
)


-- Tạo dữ liệu cho bảng ACCOUNT
INSERT INTO ACCOUNT (MaAC, username, pass, roles)
VALUES
('AC001', 'admin', '123123', 'admin'),
('AC002', 'gv_monToan', '123', 'giangvien'),
('AC003', 'gv_monAnh', '456', 'giangvien'),
('AC004', 'gv_monCNTT', '789', 'giangvien');


-- Tạo dữ liệu cho bảng SINHVIEN
INSERT INTO SINHVIEN (MaSV, TEN, Gioitinh, Ngaysinh, Sdt, Email)
VALUES
('SV001', 'Nguyen Van An', 'Nam', '2000-01-01', '123456789', 'kakaka@gmail.com'),
('SV002', 'Tran Thi Binh', 'Nu', '1999-02-02', '987654321', 'bzxccz@gmail.com'),
('SV003', 'Le Van Nghi', 'Nam', '1998-03-03', '111222333', 'ckzjz@gmail.com');

-- Tạo dữ liệu cho bảng GIANGVIEN
INSERT INTO GIANGVIEN (MaGV, TenGV, Gioitinh, Sdt, Email, MaAC)
VALUES
('GV001', 'Tran Van Xuan', 'Nam', '555666777', 'x@example.com', 'AC001'),
('GV002', 'Nguyen Thi Yen', 'Nu', '999888777', 'y@example.com', 'AC002'),
('GV003', 'Le Van Nam', 'Nam', '111333555', 'z@example.com', 'AC003');

-- Tạo dữ liệu cho bảng MON
INSERT INTO MON (MaMon, TenMon, MaGV)
VALUES
('M001', 'Mon Toan', 'GV001'),
('M002', 'Mon Anh', 'GV002'),
('M003', 'Mon CNTT', 'GV003');

-- Tạo dữ liệu cho bảng DIEM
INSERT INTO DIEM (MaSV, MaMon, Diem)
VALUES
('SV001', 'M001', 8.5),
('SV001', 'M002', 7.0),
('SV002', 'M001', 9.0),
('SV002', 'M002', 8.0),
('SV003', 'M003', 8.5);

ALTER TABLE ACCOUNT
ADD check_account varchar(20)

UPDATE GIANGVIEN
SET MaAC='AC004'
WHERE MaGV='GV001'

UPDATE MON
SET MaGV='GV002'
WHERE MaMon='M001'

UPDATE MON
SET MaGV='GV003'
WHERE MaMon='M002'

UPDATE MON
SET MaGV='GV001'
WHERE MaMon='M003'

