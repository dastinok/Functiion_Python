import begin
import estimated_cost
import property_tax


def main():
    a = begin.begin()
    b = estimated_cost.estimated_cost(a)
    property_tax.property_tax(b)



if __name__ == '__main__':
    main()