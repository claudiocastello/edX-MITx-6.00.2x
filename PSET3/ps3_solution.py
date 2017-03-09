# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import random
import pylab

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """

        if random.random() < self.clearProb:
            return True
        else:
            return False

    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """

        if random.random() <= (self.maxBirthProb * (1 - popDensity)):
            newVirus = SimpleVirus(self.getMaxBirthProb(), self.getClearProb())
            return newVirus
        else:
            raise NoChildException()



class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses


    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """

        return len(self.viruses)        


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """

        tempVirusList = self.viruses[:]
        for virus in tempVirusList:
            if virus.doesClear():
                self.viruses.remove(virus)

        popDensity = len(self.viruses) / self.getMaxPop()

        
        tempVirusList = self.viruses[:]
        for virus in tempVirusList:
            try:
                self.viruses.append(virus.reproduce(popDensity))              

            except NoChildException:
                pass

#
# PROBLEM 2
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    virusList = []
    
    for i in range(numViruses):
        virus = SimpleVirus(maxBirthProb, clearProb)
        virusList.append(virus)

    virusListCopy = virusList[:]

    patient = Patient(virusList, maxPop)


    # Simulation with numTrials
    averageList = []
    for i in range(300):
        averageList.append(0)
    
    for trial in range(numTrials):

        for step in range(300):
            tempAverage = 0
            patient.update()
            averageList[step] = (averageList[step] * trial + patient.getTotalPop()) / (trial + 1)

        patient.viruses = virusListCopy[:]

    pylab.figure('virus_pop')
    pylab.title('SimpleVirus simulation')
    pylab.xlabel('Time Steps')
    pylab.ylabel('Average Virus Population') 
    pylab.plot(averageList, 'b-', label='Growth Without Drugs')
    pylab.legend(loc='lower right')
    pylab.show()

#
# PROBLEM 3
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        """

        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb


    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        G
        """
        if drug in self.resistances.keys():
            return self.resistances[drug]
        else:
            return False
        
    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically...
        """

        # Resistance Inheritance
        newResistances = {}

        for drug in self.resistances.keys():
            if self.resistances[drug] == True:
                if random.random() > self.getMutProb():
                    newResistances[drug] = True
                else:
                    newResistances[drug] = False
            else:
                if random.random() > self.getMutProb():
                    newResistances[drug] = False
                else:
                    newResistances[drug] = True


        # Reproduction of the virus
        drugResistance = True

        for drug in activeDrugs:
            if drug in self.resistances.keys() and self.resistances[drug] == False:
                drugResistance = False

        if drugResistance == True and random.random() <= (self.maxBirthProb * (1 - popDensity)):
            newVirus = ResistantVirus(self.getMaxBirthProb(), self.getClearProb(), newResistances, self.getMutProb())
            return newVirus
        else:
            raise NoChildException()

            
class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """

        Patient.__init__(self, viruses, maxPop)
        self.activeDrugs = set()

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """

        if newDrug not in self.activeDrugs:
            self.activeDrugs.add(newDrug)        

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """

        return list(self.activeDrugs)

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """

        nonResistantCount = 0
        for virus in self.viruses:
            for drug in drugResist:
                if not virus.isResistantTo(drug):
                    nonResistantCount += 1
                    break

        return self.getTotalPop() - nonResistantCount          

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """

        tempVirusList = self.viruses[:]
        for virus in tempVirusList:
            if virus.doesClear():
                self.viruses.remove(virus)

        popDensity = len(self.viruses) / self.getMaxPop()

        
        tempVirusList = self.viruses[:]
        for virus in tempVirusList:
            try:
                self.viruses.append(virus.reproduce(popDensity, list(self.activeDrugs)))              

            except NoChildException:
                pass

#
# PROBLEM 4
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    # Creating list with numViruses and instantiating the patient
    virusList = []
    
    for i in range(numViruses):
        virus = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
        virusList.append(virus)

    virusListCopy = virusList[:]

    patient = TreatedPatient(virusList, maxPop)
    resetDrugList = patient.getPrescriptions()[:]

    # Setting up averageList
    averageList1 = []

    for i in range(300):
        averageList1.append(0)

    averageList2 = averageList1[:]

    # Simulation with numTrials without drugs    
    for trial in range(numTrials):

        for step in range(300):
            if step == 150:
                patient.addPrescription('guttagonol')
            tempAverage = 0
            patient.update()
            averageList1[step] = (averageList1[step] * trial + patient.getTotalPop()) / (trial + 1)
            averageList2[step] = (averageList2[step] * trial + patient.getResistPop(['guttagonol'])) / (trial + 1)

        patient.viruses = virusListCopy[:]
        patient.activeDrugs = resetDrugList[:]

    pylab.figure('virus_pop')
    pylab.title('Virus Population Growth Simulation')
    pylab.xlabel('Time Steps')
    pylab.ylabel('Virus Population') 
    pylab.plot(averageList1, 'b-', label='Average Total Pop Growth')
    pylab.plot(averageList2, 'r-', label='Average Resistant Pop Growth')
    pylab.legend(loc='center right')
    pylab.show()
