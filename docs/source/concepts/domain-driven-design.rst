:og:description: Domain-Driven Design (DDD) - Programming Concept

Domain-Driven Design
====================

.. title:: Domain-Driven Design (DDD) - Programming Concept  
.. meta::
    :description: DDD is an approach to software development that centers the development on programming a domain model

Domain-Driven Design (DDD) is an approach to software development that centers the development on programming a domain model that has a rich understanding of the processes and rules of a domain. 
It emphasizes collaboration between technical and domain experts to iteratively refine a conceptual model that addresses particular domain problems. 
DDD includes concepts like bounded contexts, entities, value objects, and aggregates.

.. include::  /_templates/components/signin-invite.rst

Core Concepts
-------------

The Ubiquitous Language
***********************

Think of ubiquitous language as the common tongue of your project. 
Just as medical professionals have their specific terminology that means the same thing to everyone in healthcare, DDD encourages creating a shared language between developers and domain experts.

For example, in a hospital system:

.. code-block:: java 

    // Without ubiquitous language
    class PersonProcessor {
        void processItem(PersonData item) {
            // Generic, unclear terminology
        }
    }

    // With ubiquitous language
    class AdmissionDesk {
        void admitPatient(Patient patient) {
            // Clear, domain-specific terminology
        }
    }

Bounded Contexts
****************

Bounded contexts are like departments in a hospital. 
The term "chart" means one thing in the billing department and something different in the patient ward. Each context has its own rules, terminology, and requirements.

.. code-block:: java

    // Patient Care Context
    public class Patient {
        private VitalSigns vitalSigns;
        private Medication currentMedication;
        private TreatmentPlan treatmentPlan;
        
        public void updateVitalSigns(VitalSigns newSigns) {
            // Medical domain logic
        }
    }

    // Billing Context
    public class Patient {
        private Insurance insurance;
        private BillingHistory billingHistory;
        private PaymentPlan paymentPlan;
        
        public void processPayment(Payment payment) {
            // Financial domain logic
        }
    }

Aggregates and Entities
***********************

Think of an aggregate as a medical record. 
While it contains many related pieces of information (lab results, prescriptions, notes), it's treated as one unit and always needs to maintain internal consistency.

.. code-block:: java

    public class MedicalRecord {  // Aggregate Root
        private PatientId patientId;
        private List<Prescription> prescriptions;
        private List<LabResult> labResults;
        private List<DoctorNote> notes;
        
        public void addPrescription(Prescription prescription) {
            validatePrescriptionConflicts(prescription);
            prescriptions.add(prescription);
            updateMedicationHistory();
        }
        
        private void validatePrescriptionConflicts(Prescription newPrescription) {
            // Ensure medical safety
        }
    }

Value Objects
*************

Value objects are like blood pressure readings or temperature measurements - they're defined by their attributes rather than their identity.

.. code-block:: java

    public class VitalSigns {
        private final Temperature temperature;
        private final BloodPressure bloodPressure;
        private final HeartRate heartRate;
        
        // Value objects are immutable
        public VitalSigns(Temperature temp, BloodPressure bp, HeartRate hr) {
            this.temperature = temp;
            this.bloodPressure = bp;
            this.heartRate = hr;
        }
        
        public boolean indicatesDistress() {
            return temperature.isFeverish() ||
                bloodPressure.isAbnormal() ||
                heartRate.isCritical();
        }
    }

Strategic Design
----------------

Context Mapping
***************

Just as hospitals need to coordinate between departments, bounded contexts need to interact with each other. Context mapping defines these relationships.

.. code-block:: java

    // Anti-Corruption Layer example
    public class LegacySystemAdapter {
        private LegacyPatientSystem legacySystem;
        
        public Patient translateFromLegacy(LegacyPatientRecord oldRecord) {
            return new Patient(
                new PatientId(oldRecord.getId()),
                new PersonalInfo(
                    oldRecord.getFirstName(),
                    oldRecord.getLastName(),
                    convertLegacyDateFormat(oldRecord.getBirthDate())
                )
            );
        }
    }

Domain Events
*************

Domain events are like hospital announcements - they communicate important changes that other parts of the system might need to know about.

.. code-block:: java

    public class PatientAdmitted extends DomainEvent {
        private final PatientId patientId;
        private final Ward ward;
        private final DateTime admissionTime;
        
        public PatientAdmitted(PatientId patientId, Ward ward) {
            this.patientId = patientId;
            this.ward = ward;
            this.admissionTime = DateTime.now();
        }
    }

    public class BedManagementService {
        @EventHandler
        public void on(PatientAdmitted event) {
            updateBedAvailability(event.getWard());
            notifyNursingStation(event);
            updateOccupancyRecords(event);
        }
    }

Tactical Design Patterns
------------------------

Repositories
************

Repositories provide a collection-like interface to access domain objects, hiding the complexity of data storage.

.. code-block:: java

    public interface PatientRepository {
        Patient findById(PatientId id);
        void save(Patient patient);
        List<Patient> findByWard(Ward ward);
        
        // Specific domain queries
        List<Patient> findPatientsNeedingFollowUp();
    }

Factories
*********

Factories handle the complexity of creating domain objects, ensuring they're always in a valid state.

.. code-block:: java

    public class AdmissionFactory {
        public Admission createEmergencyAdmission(
                Patient patient,
                Symptoms symptoms,
                Urgency urgency) {
            
            Ward appropriateWard = determineWard(symptoms, urgency);
            Doctor availableDoctor = findAvailableDoctor(appropriateWard);
            
            return new Admission(
                patient,
                appropriateWard,
                availableDoctor,
                AdmissionType.EMERGENCY
            );
        }
    }

Real-World Application
----------------------

Let's look at how these concepts come together in a real feature:

.. code-block:: java

    public class EmergencyAdmissionProcess {
        private final PatientRepository patients;
        private final AdmissionFactory admissionFactory;
        private final EventPublisher eventPublisher;
        
        public AdmissionResult admitEmergencyPatient(
                PatientInfo patientInfo,
                Symptoms symptoms,
                Urgency urgency) {
                
            // Create or retrieve patient
            Patient patient = patients.findById(patientInfo.getId())
                .orElseGet(() -> Patient.createNew(patientInfo));
                
            // Create admission using factory
            Admission admission = admissionFactory
                .createEmergencyAdmission(patient, symptoms, urgency);
                
            // Update patient aggregate
            patient.addAdmission(admission);
            
            // Persist changes
            patients.save(patient);
            
            // Publish domain event
            eventPublisher.publish(new PatientAdmitted(
                patient.getId(),
                admission.getWard()
            ));
            
            return new AdmissionResult(
                admission.getId(),
                admission.getWard(),
                admission.getAssignedDoctor()
            );
        }
    }

Conclusion
-----------

Domain-Driven Design isn't just about writing code - it's about understanding the problem space deeply and reflecting that understanding in your software design. 
While it requires more upfront investment in learning and modeling the domain, the resulting system is usually more maintainable and better aligned with business needs.

Remember, DDD is most valuable in complex domains with rich business logic. For simpler applications, a more straightforward approach might be more appropriate. 
The key is knowing when and how to apply these patterns effectively.

.. include::  /_templates/components/footer-links.rst
