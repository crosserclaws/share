use super::class;

#[derive(Debug, Default)]
pub struct StudentApplication {
    students: Vec<Student>,
}

impl StudentApplication {
    pub fn get_students(&self) -> &[Student] {
        self.students.as_slice()
    }

    pub fn get_student(&self, id: u32) -> Option<&Student> {
        self.students.iter().find(|&x| x.id == id)
    }

    pub fn get_student_mut(&mut self, id: u32) -> Option<&mut Student> {
        self.students.iter_mut().find(|x| x.id == id)
    }

    pub fn add_student_by_name(&mut self, name: &str) -> &Student {
        let last_id = self.students.last().map_or(0, |x| x.id);
        let s = Student::new(last_id + 1, name.to_string());
        self.students.push(s);
        self.students.last().expect("Added student")
    }

    pub fn update_student(&mut self, id: u32, description: String) -> Option<&Student> {
        self.find_student_position(id).map(|i| {
            self.students[i].description = description;
            &self.students[i]
        })
    }

    pub fn delete_student(&mut self, id: u32) -> Option<Student> {
        self.find_student_position(id).map(|i| self.students.remove(i))
    }

    fn find_student_position(&self, id: u32) -> Option<usize> {
        self.students.iter().position(|s| s.id == id)
    }
}

#[derive(Debug)]
pub struct Student {
    pub id: u32,
    pub name: String,
    pub class: class::Class,
    description: String,
}

impl Student {
    fn new(id: u32, name: String) -> Student {
        Student {
            id,
            name,
            class: class::Class::Beginner,
            description: Default::default(),
        }
    }
}
