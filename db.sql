CREATE TABLE patients (  
id INT AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(100), 
last_name VARCHAR(100),
middle_name VARCHAR(100),
passport_series_and_number VARCHAR(20),
date_of_birth DATE, 
gender VARCHAR(1),
address VARCHAR(50),  
phone_number VARCHAR(20),
email VARCHAR(100),
medical_card_number VARCHAR(20),
medical_card_issue_date DATE,
last_visit_date DATE,
next_scheduled_visit_date DATE,
insurance_policy_number VARCHAR(20),
insurance_policy_expiry_date DATE
);

CREATE TABLE procedures ( 
id AUTO_INCREMENT INT PRIMARY KEY,
type VARCHAR(100),
name VARCHAR(100),
price DECIMAL(10, 2));

CREATE TABLE patient_procedures (
patient_id INT, 
procedure_id INT,
procedure_date DATE,
doctor VARCHAR(100),
results TEXT,
FOREIGN KEY(patient_id) REFERENCES patients(id),
FOREIGN KEY(procedure_id) REFERENCES procedures(id)
);


INSERT INTO patients 
  (first_name, last_name, middle_name, passport_series_and_number, date_of_birth, gender, address, phone_number, email, medical_card_number, medical_card_issue_date, last_visit_date, next_scheduled_visit_date, insurance_policy_number, insurance_policy_expiry_date) 
VALUES 
  ('Иван', 'Иванов', 'Иванович', '4500 123456', '1980-05-15', 'M', 'ул. Ленина, д. 10', '123-456-7890', 'ivan.ivanov@example.com', 'MC12345678', '2020-01-01', '2023-04-10', '2023-05-10', 'IP1234567890', '2024-01-01'),
  ('Мария', 'Петрова', 'Игоревна', '4501 654321', '1990-07-20', 'F', 'ул. Советская, д. 5', '098-765-4321', 'maria.petrova@example.com', 'MC87654321', '2020-02-05', '2023-03-15', '2023-06-15', 'IP0987654321', '2024-02-05');

INSERT INTO procedures 
  (type, name, price) 
VALUES 
  ('Обследование', 'МРТ головного мозга', 5000.00),
  ('Анализ', 'Клинический анализ крови', 700.00),
  ('Осмотр', 'Осмотр брюшной полости', 900.00)
  ('Лабороторные исследования', 'Резултаты забора крови' 990.00),
  ('Прививки', 'Вакцинация', 1000.00);

INSERT INTO patient_procedures 
  (patient_id, procedure_id, procedure_date, doctor, results) 
VALUES 
  (1, 1, '2023-04-15', 'Алексеев А. Е.', 'Не обнаружено патологий'),
  (1, 2, '2023-04-12', 'Борисова Б. Б.', 'В пределах нормы');
