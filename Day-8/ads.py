class Subscription:
  def features(self):
    print("Watch videos with advertisements")
class PremiumSubscription(Subscription):
  def features(self):
    print("Watch videos without advertisements")
ps=PremiumSubscription()
ps.features()
s=Subscription()
s.features()