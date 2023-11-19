use super::student::Student;

#[derive(Debug, Default)]
pub struct ClassApplication {
}

impl ClassApplication {
    pub fn to_next_level_class(&self, s: &mut Student) -> Result<(), String> {
        match s.class.level_up() {
            Some(cls) => {
                s.class = cls;
                println!("{:?}", s);
                Ok(())
            },
            None => Err(format!("Student(id: {}, name: {}) is already in the highest class.", s.id, s.name)),
        }
    }

    pub fn to_prev_level_class(&self, s: &mut Student) -> Result<(), String> {
        match s.class.level_down() {
            Some(cls) => {
                s.class = cls;
                println!("{:?}", s);
                Ok(())
            },
            None => Err(format!("Student(id: {}, name: {}) is already in the lowest class.", s.id, s.name)),
        }
    }
}

#[derive(Debug)]
pub enum Class {
    Beginner,
    Intermediate,
    Advanced,
    Expert,
}

impl Class {
    fn level_up(&self) -> Option<Class> {
        match self {
            Self::Beginner => Some(Self::Intermediate),
            Self::Intermediate => Some(Self::Advanced),
            Self::Advanced => Some(Self::Expert),
            Self::Expert => None,
        }
    }

    fn level_down(&self) -> Option<Class> {
        match self {
            Self::Beginner => None,
            Self::Intermediate => Some(Self::Beginner),
            Self::Advanced => Some(Self::Intermediate),
            Self::Expert => Some(Self::Advanced),
        }
    }
}
