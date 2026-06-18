'''
(1) Phân Tích Ngắn Gọn (Code Review) 

Lỗi IndexError tại dòng r = p[2]: Bản ghi của Levi có đầy đủ 3 phần tử (chỉ mục từ 0 đến 2) nên truy cập được p[2]. Bản ghi của SofM chỉ có 2 phần tử ("SofM", 150) (chỉ mục 0 và 1), việc cố truy cập chỉ mục số 2 vượt quá phạm vi của tuple gây sập chương trình. 

Lỗi khi xử lý Optimus: Chương trình sẽ sập ở dòng tính toán tiền thưởng b = (m * 10) + (int(r) * 0.5). Tên ngoại lệ in ra sẽ là ValueError vì hàm int() không thể chuyển đổi chuỗi chữ "N/A" thành số nguyên. 

Kỹ năng Debug với print(): Giúp xác định chính xác bản ghi cụ thể nào đang được xử lý ngay trước khi hệ thống crash, cô lập dữ liệu lỗi để sửa đổi mà không cần đoán mò. 



'''

player_records = [ 
   ("Levi", 120, 2500), 
   ("SofM", 150), 
   ("Optimus", 100, "N/A"), 
   ("Archie", 90, 2100) 
] 
 
def calculate_bonus(matches, mmr): 
   return (matches * 10) + (int(mmr) * 0.5) 
 
def process_end_of_season_bonus(player_list): 
   print("--- BẢNG TÍNH THƯỞNG RP ---") 
   for record in player_list: 
       name = record[0] 
       try: 
           matches = record[1] 
           mmr = record[2] 
            
           bonus = calculate_bonus(matches, mmr) 
           print(f"Tuyển thủ {name} nhận được {bonus} RP") 
            
       except IndexError: 
           print(f"{name}: Lỗi - Hồ sơ bị thiếu thông tin!") 
       except ValueError: 
           print(f"{name}: Lỗi - Dữ liệu MMR không hợp lệ!") 
 
if __name__ == "__main__": 
   process_end_of_season_bonus(player_records) 

 