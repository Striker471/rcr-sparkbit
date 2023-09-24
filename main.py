from RoboticCodeRepresentationGenerator import RoboticCodeRepresentationGenerator

if __name__ == '__main__':
    command_logs = ["LEFT", "GRAB", "LEFT", "BACK", "LEFT", "BACK", "LEFT"]
    generator_RCR = RoboticCodeRepresentationGenerator(command_logs)
    print(generator_RCR.get_rcr("LEFT"))
