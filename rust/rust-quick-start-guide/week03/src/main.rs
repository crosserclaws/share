mod class;
mod student;

use std::io;

#[derive(Debug, Default)]
struct StudentManagementSystem {
    student: student::StudentApplication,
    class: class::ClassApplication,
}

impl StudentManagementSystem {
    pub fn list_students(&self) -> Result<(), String> {
        println!("[List Students]");
        let students = self.student.get_students();
        if students.is_empty() {
            println!("Empty");
        }
        for s in students {
            println!("ID: {}, Name: {}", s.id, s.name);
        }
        Ok(())
    }

    pub fn show_student(&self) -> Result<(), String> {
        println!("[Show Student]");
        println!("Please enter a student id: ");
        let id = Self::read_id()?;
        match self.student.get_student(id) {
            Some(student) => println!("{:?}", student),
            None => return Err(format!("Cannot find a student with id: {}", id)),
        }
        Ok(())
    }

    pub fn add_student(&mut self) -> Result<(), String> {
        println!("[Add Student]");
        println!("Please enter a new student name: ");
        let name = Self::read_input_string()?;
        let student_name = name.trim();
        if student_name.is_empty() {
            return Err("Student name cannot be empty.".to_string());
        }
        let student = self.student.add_student_by_name(student_name);
        println!("Student added: {:?}", student);
        Ok(())
    }

    pub fn update_student(&mut self) -> Result<(), String> {
        println!("[Update Student]");
        println!("Please enter a student id: ");
        let id = Self::read_id()?;

        if let Some(_) = self.student.get_student(id) {
            println!("Please enter new student description: ");
            let description = Self::read_input_string()?;
            let student_description = description.trim();
            if student_description.is_empty() {
                return Err("Student description cannot be empty.".to_string());
            }
            match self.student.update_student(id, student_description.to_string()) {
                Some(student) => println!("Student updated: {:?}", student),
                None => return Err(format!("Cannot find a student with id: {}", id)),
            }
        } else {
            return Err(format!("Cannot find a student with id: {}", id));
        }
        Ok(())
    }

    pub fn delete_student(&mut self) -> Result<(), String> {
        println!("[Delete Student]");
        println!("Please enter a student id: ");
        let id = Self::read_id()?;
        match self.student.delete_student(id) {
            Some(student) => println!("{:?}", student),
            None => return Err(format!("Cannot find a student with id: {}", id)),
        }
        Ok(())
    }

    pub fn upgrade_student(&mut self) -> Result<(), String> {
        println!("[Upgrade Student]");
        println!("Please enter a student id: ");
        let id = Self::read_id()?;
        match self.student.get_student_mut(id) {
            Some(s) => self.class.to_next_level_class(s)?,
            None => return Err(format!("Cannot find a student with id: {}", id)),
        }
        Ok(())
    }

    pub fn downgrade_student(&mut self) -> Result<(), String> {
        println!("[Downgrade Student]");
        println!("Please enter a student id: ");
        let id = Self::read_id()?;
        match self.student.get_student_mut(id) {
            Some(s) => self.class.to_prev_level_class(s)?,
            None => return Err(format!("Cannot find a student with id: {}", id)),
        }
        Ok(())
    }

    fn read_id() -> Result<u32, String> {
        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .map_err(|error| format!("Error reading input: {}", error))?;
        input
            .trim()
            .parse::<u32>()
            .map_err(|error| format!("Error reading input: {}", error))
    }

    fn read_input_string() -> Result<String, String> {
        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .map_err(|error| format!("Error reading input: {}", error))?;
        Ok(input)
    }
}

fn main() {
    let mut s = StudentManagementSystem::default();
    initialize(&mut s);

    loop {
        println!("[Menu]");
        println!("0) Exit");
        println!("1) List all students");
        println!("2) Show a student");
        println!("3) Add a student");
        println!("4) Update a student");
        println!("5) Delete a student");
        println!("6) Upgrade a student");
        println!("7) Downgrade a student");
        println!("Please enter a number for a operation: ");
        let mut input = String::new();
        let result = match parse_operation(&mut input) {
            Ok(Operation::Exit) => break,
            Ok(Operation::ListAllStudents) => s.list_students(),
            Ok(Operation::ShowStudent) => s.show_student(),
            Ok(Operation::AddStudent) => s.add_student(),
            Ok(Operation::UpdateStudent) => s.update_student(),
            Ok(Operation::DeleteStudent) => s.delete_student(),
            Ok(Operation::UpgradeStudent) => s.upgrade_student(),
            Ok(Operation::DowngradeStudent) => s.downgrade_student(),
            Err(error) => Err(format!("Failed to parse the operation: {error:?}")),
        };
        if let Err(error) = result {
            eprintln!("{error}");
        }

        println!();
    }
}

#[derive(Debug)]
enum Operation {
    Exit = 0,
    ListAllStudents,
    ShowStudent,
    AddStudent,
    UpdateStudent,
    DeleteStudent,
    UpgradeStudent,
    DowngradeStudent,
}

#[derive(Debug)]
enum ParseOperationError {
    InvalidInput(String),
    InvalidOperation(String),
}

fn parse_operation(input: &mut String) -> Result<Operation, ParseOperationError> {
    match io::stdin().read_line(input) {
        Ok(_) => match input.trim().parse::<u8>() {
            Ok(op) => Ok(match op {
                0 => Operation::Exit,
                1 => Operation::ListAllStudents,
                2 => Operation::ShowStudent,
                3 => Operation::AddStudent,
                4 => Operation::UpdateStudent,
                5 => Operation::DeleteStudent,
                6 => Operation::UpgradeStudent,
                7 => Operation::DowngradeStudent,
                _ => {
                    return Err(ParseOperationError::InvalidOperation(format!(
                        "Invalid operation: {}",
                        input.trim()
                    )))
                }
            }),
            Err(_) => Err(ParseOperationError::InvalidInput(
                "Invalid input".to_string(),
            )),
        },
        Err(error) => Err(ParseOperationError::InvalidInput(format!(
            "Error reading input: {}",
            error
        ))),
    }
}

fn initialize(sms: &mut StudentManagementSystem) {
    sms.student.add_student_by_name("Alice");
    sms.student.add_student_by_name("Bob");
    sms.student.add_student_by_name("Cindy");
    sms.student.add_student_by_name("David");
}
